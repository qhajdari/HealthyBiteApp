from abc import ABC, abstractmethod
from app.models.recipe_models import Recipe

class AbstractRecipeService(ABC):
    @abstractmethod
    def add_recipe(self, name: str, category: str, ingredients: str, instructions: str, prep_time: int) -> Recipe:
        pass

    @abstractmethod
    def get_all_recipes(self) -> list[Recipe]:
        pass

    @abstractmethod
    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        pass
