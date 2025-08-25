# tests/test_recipe_service.py  (ose app/tests/...)
import unittest

from app import create_app, db
from app.services.concrete_recipe_service import RecipeService
from app.services.exceptions import InvalidRecipeException
from app.models.recipe_models import Recipe, RecipeCategory

class TestRecipeService(unittest.TestCase):
    def setUp(self):
        # krijo app specifik per test me DB per memorije
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        })
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self.service = RecipeService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.engine.dispose()      # mbyll lidhjet e hapura
        self.ctx.pop()



    def test_add_recipe_valid_category(self):
        recipe = self.service.add_recipe(
            name="Avocado Salad",
            category="VEGAN",
            ingredients="Avocado, Tomato, Onion",
            instructions="Mix all together",
            prep_time=10
        )
        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(recipe.category, RecipeCategory.VEGAN.value)
        self.assertEqual(Recipe.query.count(), 1)

    def test_add_recipe_invalid_category(self):
        with self.assertRaises(InvalidRecipeException):
            self.service.add_recipe(
                name="Bad Recipe",
                category="INVALID",
                ingredients="None",
                instructions="None",
                prep_time=5
            )

if __name__ == "__main__":
    unittest.main()
