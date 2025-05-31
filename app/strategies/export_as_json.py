import json
from app.strategies.export_strategy import ExportStrategy


class ExportAsJSON:
    def export(self, recipes):
        data = []
        for recipe in recipes:
            data.append({
                "name": recipe.name,
                "category": recipe.category,
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "prep_time": recipe.prep_time
            })
        return json.dumps(data, indent=2)
