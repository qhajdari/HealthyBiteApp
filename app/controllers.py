from flask import render_template, request, redirect, url_for, session, flash, make_response
from app import db
from app.models.recipe_models import Recipe, MealPlan
from app.services.concrete_recipe_service import RecipeService
from app.services.exceptions import InvalidRecipeException
from app.services.user_service import authenticate
from functools import wraps
from app.strategies.export_as_text import ExportAsText
from app.strategies.export_as_json import ExportAsJSON
from app.strategies.recipe_exporter import RecipeExporter

recipe_service = RecipeService()
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def register_routes(app):  # ⬅️ Tani funksioni merr app si argument

    @app.route('/')
    def index():
        recipes = recipe_service.get_all_recipes()
        return render_template('index.html', recipes=recipes)

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    @role_required("Premium")
    def add_recipe():
        error = None
        if request.method == 'POST':
            name = request.form['name']
            category = request.form['category']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            prep_time_input = request.form['prep_time']

            try:
                prep_time = int(prep_time_input)
                recipe_service.add_recipe(name, category, ingredients, instructions, prep_time)
                return redirect(url_for('index'))
            except (ValueError, InvalidRecipeException) as e:
                error = str(e)

        return render_template('add_recipe.html', error=error)

    @app.route('/meal_planner', methods=['GET', 'POST'])
    @login_required
    @role_required("Regular", "Premium")
    def meal_planner():
        recipes = recipe_service.get_all_recipes()
        if request.method == 'POST':
            MealPlan.query.delete()
            db.session.commit()
            for day in DAYS_OF_WEEK:
                recipe_id = request.form.get(day)
                if recipe_id and recipe_id != 'None':
                    plan = MealPlan(day=day, recipe_id=int(recipe_id))
                    db.session.add(plan)
            db.session.commit()
            return redirect(url_for('meal_planner'))

        plans = {plan.day: plan.recipe_id for plan in MealPlan.query.all()}
        return render_template('meal_planner.html', days=DAYS_OF_WEEK, recipes=recipes, plans=plans)
    

    @app.route('/export_recipes/<format>')
    @login_required
    @role_required("Premium")
    def export_recipes(format):
        recipes = recipe_service.get_all_recipes()

        if format == "text":
            exporter = RecipeExporter(ExportAsText())
            content = exporter.export(recipes)
            response = make_response(content)
            response.headers["Content-Type"] = "text/plain"
            response.headers["Content-Disposition"] = "attachment; filename=recipes.txt"
            return response

        elif format == "json":
            exporter = RecipeExporter(ExportAsJSON())
            content = exporter.export(recipes)
            response = make_response(content)
            response.headers["Content-Type"] = "application/json"
            response.headers["Content-Disposition"] = "attachment; filename=recipes.json"
            return response

        return "Invalid export format", 400

    @app.route('/shopping_list')
    @login_required
    @role_required("Regular", "Premium") 
    def shopping_list():
        plans = MealPlan.query.all()
        ingredients = []
        for plan in plans:
            ingr_list = plan.recipe.ingredients.split(',')
            ingredients.extend([i.strip() for i in ingr_list])
        unique_ingredients = sorted(set(ingredients))
        return render_template('shopping_list.html', ingredients=unique_ingredients)


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = authenticate(username, password)
            if user:
                session['user'] = user.username
                session['role'] = user.get_role()

                
                role = user.get_role()
                if role == "Admin":
                    return redirect(url_for('admin_panel'))
                elif role == "Premium":
                    return redirect(url_for('premium_panel'))
                elif role == "Regular":
                    return redirect(url_for('regular_panel'))

                else:
                    return redirect(url_for('index'))

            else:
                error = "Invalid username or password!"
        return render_template('login.html', error=error)



    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
    


    @app.route('/admin_panel')
    @login_required
    def admin_panel():
        if session.get('role') != 'Admin':
            return "Unauthorized", 403
        recipes = recipe_service.get_all_recipes()
        return render_template('admin_panel.html', recipes=recipes)

    
    
    @app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
    @login_required
    def delete_recipe(recipe_id):
        if session.get('role') != 'Admin':
            return "Unauthorized", 403

        recipe = Recipe.query.get(recipe_id)
        if recipe:
            db.session.delete(recipe)
            db.session.commit()
        return redirect(url_for('admin_panel'))

    @app.route('/regular_panel')
    @login_required
    @role_required("Regular")
    def regular_panel():
        return render_template('regular_panel.html')
    

    @app.route('/premium_panel')
    @login_required
    @role_required("Premium")
    def premium_panel():
        return render_template('premium_panel.html')





def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper


def role_required(*roles):
    def wrapper_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                return "Unauthorized", 403
            return f(*args, **kwargs)
        return wrapped
    return wrapper_decorator
