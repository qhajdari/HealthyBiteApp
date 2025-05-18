import json
from app.strategies.export_strategy import ExportStrategy

class ExportAsJSON(ExportStrategy):
    def export(self, recipe):
        return json.dumps({
            "name": recipe.name,
            "category": recipe.category,
            "ingredients": recipe.ingredients.split(","),
            "instructions": recipe.instructions,
            "prep_time": recipe.prep_time
        }, indent=2)
