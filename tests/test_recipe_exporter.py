import unittest
import os
import json
import csv

from app.strategies.recipe_exporter import CSVRecipeExporter, JSONRecipeExporter

class DummyRecipe:
    """Dummy class që imiton modelin Recipe për testim."""
    def __init__(self, id, name, category, ingredients, instructions, prep_time):
        self.id = id
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time

class TestRecipeExporters(unittest.TestCase):
    def setUp(self):
        self.recipes = [
            DummyRecipe(1, "Pasta", "VEGAN", "Pasta, Tomato", "Boil pasta", 15),
            DummyRecipe(2, "Salad", "VEGETARIAN", "Lettuce, Tomato", "Mix together", 5),
        ]
        self.csv_file = "test_recipes.csv"
        self.json_file = "test_recipes.json"

    def tearDown(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_csv_exporter(self):
        exporter = CSVRecipeExporter()
        exporter.export(self.recipes, self.csv_file)
        self.assertTrue(os.path.exists(self.csv_file))

        with open(self.csv_file, newline='', encoding="utf-8") as f:
            rows = list(csv.reader(f))

        self.assertEqual(rows[0], ['ID', 'Name', 'Category', 'Ingredients', 'Instructions', 'Prep Time'])
        self.assertEqual(len(rows) - 1, 2)

    def test_json_exporter(self):
        exporter = JSONRecipeExporter()
        exporter.export(self.recipes, self.json_file)
        self.assertTrue(os.path.exists(self.json_file))

        with open(self.json_file, encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Pasta")
        self.assertEqual(data[1]["category"], "VEGETARIAN")

if __name__ == "__main__":
    unittest.main()
