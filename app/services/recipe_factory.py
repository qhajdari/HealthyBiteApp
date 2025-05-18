from app.models import Recipe
from app.services.exceptions import InvalidRecipeException

class RecipeFactory:
    @staticmethod
    def create_recipe(name, category, ingredients, instructions, prep_time):
        if not name or not ingredients or not instructions or prep_time <= 0:
            raise InvalidRecipeException("Recipe data is incomplete or invalid.")
        
        return Recipe(
            name=name,
            category=category,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )
