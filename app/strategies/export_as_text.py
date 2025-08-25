from typing import Iterable
from app.models.recipe_models import Recipe
from app.strategies.export_strategy import ExportStrategy

class ExportAsText(ExportStrategy):
    def export(self, recipes: Iterable[Recipe]) -> str:
        lines = []
        for r in recipes:
            lines.append(f"Name: {r.name}")
            lines.append(f"Category: {r.category}")
            lines.append(f"Ingredients: {r.ingredients}")
            lines.append(f"Instructions: {r.instructions}")
            lines.append(f"Prep Time: {r.prep_time} minutes")
            lines.append("-" * 40)
        return "\n".join(lines)
