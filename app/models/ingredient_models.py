# models/ingredient_models.py
from abc import ABC, abstractmethod
from app import db

class Ingredient(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Vegetable(Ingredient):
    def get_type(self):
        return "Vegetable"


class Fruit(Ingredient):
    def get_type(self):
        return "Fruit"


class Protein(Ingredient):
    def get_type(self):
        return "Protein"
