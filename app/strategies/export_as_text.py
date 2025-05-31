from app.strategies.export_strategy import ExportStrategy

class ExportAsText:
    def export(self, recipes):
        output = ""
        for recipe in recipes:
            output += f"Name: {recipe.name}\n"
            output += f"Category: {recipe.category}\n"
            output += f"Ingredients: {recipe.ingredients}\n"
            output += f"Instructions: {recipe.instructions}\n"
            output += f"Prep Time: {recipe.prep_time} minutes\n"
            output += "-" * 40 + "\n"
        return output
