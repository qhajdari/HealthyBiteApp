from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import MealPlan
from app.services.concrete_recipe_service import RecipeService
from app.services.exceptions import InvalidRecipeException

# Create an instance of the RecipeService
recipe_service = RecipeService()

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

@app.route('/')
def index():
    recipes = recipe_service.get_all_recipes()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            prep_time_input = request.form['prep_time']

            # Convert prep_time to an integer
            if not name or not category or not ingredients or not instructions or not prep_time_input:
                raise InvalidRecipeException("All fields are required.")
            prep_time = int(prep_time_input)

            # Thirrja e shërbimit që mund të ngrejë përjashtim
            recipe_service.add_recipe(name, category, ingredients, instructions, prep_time)
            return redirect(url_for('index'))

        except (ValueError, InvalidRecipeException) as e:
            error = str(e)

    return render_template('add_recipe.html', error=error)

@app.route('/meal_planner', methods=['GET', 'POST'])
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

@app.route('/shopping_list')
def shopping_list():
    plans = MealPlan.query.all()
    ingredients = []
    for plan in plans:
        ingr_list = plan.recipe.ingredients.split(',')
        ingredients.extend([i.strip() for i in ingr_list])
    unique_ingredients = sorted(set(ingredients))
    return render_template('shopping_list.html', ingredients=unique_ingredients)
