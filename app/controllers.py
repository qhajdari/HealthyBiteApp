from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Recipe, MealPlan

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thirsday', 'Friday', 'Saturday', 'Sunday']

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        prep_time = int(request.form['prep_time'])

        recipe = Recipe(
            name=name,
            category=category,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/meal_planner', methods=['GET', 'POST'])
def meal_planner():
    recipes = Recipe.query.all()
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
