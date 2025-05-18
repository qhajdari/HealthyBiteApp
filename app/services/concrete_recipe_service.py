from app import db
from app.models import Recipe
from app.services.abstract_recipe_service import AbstractRecipeService
from app.services.exceptions import InvalidRecipeException
from app.models import RecipeCategory


class RecipeService(AbstractRecipeService):
    def add_recipe(self, name, category, ingredients, instructions, prep_time):
        if category not in RecipeCategory.__members__:
            raise InvalidRecipeException("Category is not valid.")

        new_recipe = Recipe(
            name=name,
            category=category,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe

    def get_all_recipes(self) -> list[Recipe]:
        return Recipe.query.all()

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        return Recipe.query.get(recipe_id)
