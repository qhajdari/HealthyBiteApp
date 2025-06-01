from enum import Enum
from app import db

class RecipeCategory(Enum):
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    KETO = "Keto"
    LOW_CARB = "Low Carb"

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)

class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe')
