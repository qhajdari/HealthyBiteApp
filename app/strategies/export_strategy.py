from abc import ABC, abstractmethod
from app.models import Recipe

class ExportStrategy(ABC):
    @abstractmethod
    def export(self, recipe: Recipe) -> str:
        pass
