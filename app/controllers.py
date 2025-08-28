from __future__ import annotations
from functools import wraps

from flask import render_template, request, redirect, url_for, session, flash, make_response
from app import db
from app.models.recipe_models import Recipe, MealPlan, RecipeCategory
from app.services.concrete_recipe_service import RecipeService
from app.services.exceptions import InvalidRecipeException
from app.services.user_service import authenticate
from app.services.logger_service import LoggerService
from app.services.stats_service import threaded_stats

from app.strategies.export_as_text import ExportAsText
from app.strategies.export_as_json import ExportAsJSON

logger = LoggerService()
recipe_service = RecipeService()
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# ------------------ Decorators ------------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

def role_required(*roles):
    roles_norm = tuple(r.title() for r in roles)
    def wrapper_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            role = session.get('role', '')
            if role.title() not in roles_norm:
                return "Unauthorized", 403
            return f(*args, **kwargs)
        return wrapped
    return wrapper_decorator


# ------------------ Route Registration ------------------
def register_routes(app):

    @app.route('/')
    def index():
        recipes = recipe_service.get_all_recipes()
        return render_template('index.html', recipes=recipes)

    # -------- Auth --------
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            user = authenticate(username, password)
            if user:
                session['user'] = user.username
                session['role'] = user.get_role()
                logger.log(f"User '{user.username}' logged in as {user.get_role()}")

                # Redirect sipas rolit
                role = user.get_role()
                if role == "Admin":
                    return redirect(url_for('admin_panel'))
                elif role == "Premium":
                    return redirect(url_for('premium_panel'))
                elif role == "Regular":
                    return redirect(url_for('regular_panel'))
                return redirect(url_for('index'))
            else:
                error = "Invalid username or password!"
                flash(error, "danger")
                logger.log(f"Failed login attempt for username '{username}'")
        return render_template('login.html', error=error)

    @app.route('/logout')
    def logout():
        session.clear()
        flash("Logged out.", "info")
        return redirect(url_for('login'))

    # -------- Recipe: Add / List --------
    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    @role_required("Premium")  # vetëm Premium lejohet të shtojë
    def add_recipe():
        error = None
        if request.method == 'POST':
            name = request.form.get('name', '')
            category = request.form.get('category', '')
            ingredients = request.form.get('ingredients', '')
            instructions = request.form.get('instructions', '')
            prep_time_input = request.form.get('prep_time', '')

            try:
                prep_time = int(prep_time_input)
                # KERKESA: kategoria si Enum NAME p.sh. VEGAN, VEGETARIAN, ...
                recipe_service.add_recipe(name, category, ingredients, instructions, prep_time)
                flash("Recipe added.", "success")
                return redirect(url_for('index'))
            except ValueError:
                error = "Prep time must be an integer."
            except InvalidRecipeException as e:
                error = str(e)

            if error:
                flash(error, "danger")
        # dërgo listën e kategorive në view (Enum names)
        enum_names = [m.name for m in RecipeCategory]
        return render_template('add_recipe.html', error=error, categories=enum_names)

    # -------- Meal Planner --------
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
                    db.session.add(MealPlan(day=day, recipe_id=int(recipe_id)))
            db.session.commit()
            flash("Weekly plan saved.", "success")
            return redirect(url_for('meal_planner'))

        plans = {plan.day: plan.recipe_id for plan in MealPlan.query.all()}
        return render_template('meal_planner.html', days=DAYS_OF_WEEK, recipes=recipes, plans=plans)

    # -------- Export (Strategy Pattern) --------
    @app.route('/export_recipes/<format>')
    @login_required
    @role_required("Premium")
    def export_recipes(format: str):
        recipes = recipe_service.get_all_recipes()

        if format == "text":
            content = ExportAsText().export(recipes)
            resp = make_response(content)
            resp.headers["Content-Type"] = "text/plain"
            resp.headers["Content-Disposition"] = "attachment; filename=recipes.txt"
            return resp

        elif format == "json":
            content = ExportAsJSON().export(recipes)
            resp = make_response(content)
            resp.headers["Content-Type"] = "application/json"
            resp.headers["Content-Disposition"] = "attachment; filename=recipes.json"
            return resp

        return "Invalid export format", 400

    # -------- Shopping List --------
    @app.route('/shopping_list')
    @login_required
    @role_required("Regular", "Premium")
    def shopping_list():
        plans = MealPlan.query.all()
        ingredients = []
        for plan in plans:
            if plan.recipe and plan.recipe.ingredients:
                ingr_list = plan.recipe.ingredients.split(',')
                ingredients.extend([i.strip() for i in ingr_list])
        unique_ingredients = sorted(set(ingredients))
        return render_template('shopping_list.html', ingredients=unique_ingredients)

    # -------- Stats (threaded) --------
    @app.route('/stats')
    @login_required
    @role_required("Regular", "Premium", "Admin")
    def stats():
        times = [r.prep_time for r in Recipe.query.all() if isinstance(r.prep_time, int)]
        stats_data = threaded_stats(times)
        return render_template('stats.html', count=len(times), stats=stats_data)

    # -------- Role dashboards --------
    @app.route('/admin_panel')
    @login_required
    @role_required("Admin")
    def admin_panel():
        recipes = recipe_service.get_all_recipes()
        return render_template('admin_panel.html', recipes=recipes)

    @app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
    @login_required
    @role_required("Admin")
    def delete_recipe(recipe_id: int):
        recipe = Recipe.query.get(recipe_id)
        if recipe:
            db.session.delete(recipe)
            db.session.commit()
            flash("Recipe deleted.", "info")
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
