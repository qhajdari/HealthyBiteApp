import unittest
from app.strategies.export_as_json import ExportAsJSON
from app.strategies.export_as_text import ExportAsText

class DummyRecipe:
    def __init__(self, name, category, ingredients, instructions, prep_time):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time

class TestExportStrategies(unittest.TestCase):
    def setUp(self):
        self.recipes = [
            DummyRecipe("Pasta", "Vegan", "Pasta, Tomato", "Boil pasta", 15),
            DummyRecipe("Salad", "Vegetarian", "Lettuce, Tomato", "Mix", 5),
        ]

    def test_export_as_json(self):
        exporter = ExportAsJSON()
        out = exporter.export(self.recipes)
        self.assertIn('"name": "Pasta"', out)
        self.assertIn('"category": "Vegetarian"', out)
        self.assertIn('"prep_time": 5', out)

    def test_export_as_text(self):
        exporter = ExportAsText()
        out = exporter.export(self.recipes)
        self.assertIn("Name: Pasta", out)
        self.assertIn("Category: Vegetarian", out)
        self.assertIn("Prep Time: 5 minutes", out)

if __name__ == "__main__":
    unittest.main()
