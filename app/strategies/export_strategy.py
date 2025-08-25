from abc import ABC, abstractmethod
from typing import Iterable
from app.models.recipe_models import Recipe

class ExportStrategy(ABC):
    @abstractmethod
    def export(self, recipes: Iterable[Recipe]) -> str:
        """Return a string representation of the exported recipes."""
        pass
