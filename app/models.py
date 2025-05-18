from app import db
from enum import Enum

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    prep_time = db.Column(db.Integer)

class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe')

class RecipeCategory(Enum):
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    LOW_CARB = "Low Carb"
    KETO = "Keto"
    SNACK = 'Snack'
    DESSERT = 'Dessert'
