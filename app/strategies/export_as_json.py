import json
from typing import Iterable
from app.models.recipe_models import Recipe
from app.strategies.export_strategy import ExportStrategy

class ExportAsJSON(ExportStrategy):
    def export(self, recipes: Iterable[Recipe]) -> str:
        data = []
        for r in recipes:
            data.append({
                "name": r.name,
                "category": r.category,
                "ingredients": r.ingredients,
                "instructions": r.instructions,
                "prep_time": r.prep_time,
            })
        return json.dumps(data, ensure_ascii=False, indent=2)
