from app.strategies.export_strategy import ExportStrategy

class ExportAsText(ExportStrategy):
    def export(self, recipe):
        return f"Recipe: {recipe.name}\nCategory: {recipe.category}\nIngredients: {recipe.ingredients}\nInstructions: {recipe.instructions}"
