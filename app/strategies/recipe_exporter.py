# app/strategies/recipe_exporter.py
import csv
import json
from abc import ABC, abstractmethod
import io

class RecipeExporter(ABC):
    @abstractmethod
    def export(self, recipes, file_path: str) -> None:
        """Export a list of recipe-like objects to a file."""
        pass

class CSVRecipeExporter(RecipeExporter):
    def export(self, recipes, file_path: str) -> None:
        # recipes: list of objects or dicts
        # shkruaj CSV në disk
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Category', 'Ingredients', 'Instructions', 'Prep Time'])
            for r in recipes:
                # lexo atribute në mënyrë tolerante (objekt apo dict)
                get = (lambda k, default="": getattr(r, k, getattr(r, k, default)))  # not elegant, but safe
                row = [
                    getattr(r, "id", r.get("id", None)) if isinstance(r, dict) else getattr(r, "id", None),
                    getattr(r, "name", r.get("name", "")) if isinstance(r, dict) else getattr(r, "name", ""),
                    getattr(r, "category", r.get("category", "")) if isinstance(r, dict) else getattr(r, "category", ""),
                    getattr(r, "ingredients", r.get("ingredients", "")) if isinstance(r, dict) else getattr(r, "ingredients", ""),
                    getattr(r, "instructions", r.get("instructions", "")) if isinstance(r, dict) else getattr(r, "instructions", ""),
                    getattr(r, "prep_time", r.get("prep_time", 0)) if isinstance(r, dict) else getattr(r, "prep_time", 0),
                ]
                writer.writerow(row)

class JSONRecipeExporter(RecipeExporter):
    def export(self, recipes, file_path: str) -> None:
        # recipes: list of dicts or simple objects
        payload = []
        for r in recipes:
            if isinstance(r, dict):
                payload.append(r)
            else:
                payload.append({
                    "id": getattr(r, "id", None),
                    "name": getattr(r, "name", ""),
                    "category": getattr(r, "category", ""),
                    "ingredients": getattr(r, "ingredients", ""),
                    "instructions": getattr(r, "instructions", ""),
                    "prep_time": getattr(r, "prep_time", 0),
                })
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

__all__ = ["RecipeExporter", "CSVRecipeExporter", "JSONRecipeExporter"]
