from app import db
from app.models.recipe_models import Recipe
from app.services.abstract_recipe_service import AbstractRecipeService
from app.services.exceptions import InvalidRecipeException
from app.models.recipe_models import RecipeCategory
from app.services.recipe_factory import RecipeFactory



class RecipeService(AbstractRecipeService):
    def add_recipe(self, name, category, ingredients, instructions, prep_time):
        if category not in RecipeCategory.__members__:
            raise InvalidRecipeException("Category is not valid.")

        new_recipe = RecipeFactory.create_recipe(
            name=name,
            category=RecipeCategory[category].value,
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
