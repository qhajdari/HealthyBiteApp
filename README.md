# HealthyBiteApp

**HealthyBiteApp** is a web-based meal planning and recipe management application developed using **Python Flask**, following **Object-Oriented Programming (OOP)** principles and **MVC architecture**. It helps users plan healthy meals, manage recipes, and generate smart shopping lists based on weekly meal plans.

---

## 👨‍💻 Project Info
- **Project Name:** HealthyBite  
- **Author:** Qëndresa Hajdari  

---

## 🎯 Project Purpose
The goal of HealthyBiteApp is to help individuals maintain a healthy diet through:

- Browsing healthy recipes (categorized by dietary preferences)  
- Planning meals throughout the week  
- Automatically generating shopping lists  
- Exporting recipe information in multiple formats  

---

## 💡 Features
- ✅ Add, view, and manage healthy recipes  
- ✅ Assign meals to specific days of the week  
- ✅ Auto-generate shopping list from planned meals  
- ✅ Export recipe data in JSON or text format  
- ✅ Role-based user model (Regular, Premium, Admin)  
- ✅ Elegant user interface built with Bootstrap  
- ✅ Uses SQLite as the database  

---

## 🧠 OOP Concepts & Design Patterns

| Concept                     | Implemented With                                    |
|------------------------------|-----------------------------------------------------|
| **Abstraction / Interface** | `AbstractRecipeService`, `ExportStrategy`, `User`, `Ingredient`, `RecipeExporter(ABC)` |
| **Inheritance (3 levels)**  | `User → RegularUser → PremiumUser`                  |
| **Polymorphism**            | `get_role()` and `export()` methods                 |
| **Exception Handling**      | `InvalidRecipeException`                            |
| **Enum**                    | `RecipeCategory`                                    |
| **Design Patterns**         | Factory (`RecipeFactory`), Singleton (`LoggerService`), Strategy (`ExportAsJSON`, `ExportAsText`, `CSV/JSONRecipeExporter`) |
| **Architecture**            | MVC (Model–View–Controller)                         |

---

## 🧪 Tests & Coverage
All core components of the application are covered with **unit tests**.  

### Coverage Report
```bash
coverage run -m unittest discover -s tests -p "test_*.py"
coverage report -m
```
## Test Mapping

| Test File                         | What it Covers                              |
| --------------------------------- | ------------------------------------------- |
| `test_recipe_service.py`          | Adding recipes, invalid categories          |
| `test_recipe_exporter.py`         | CSV and JSON exporters (file-based)         |
| `test_export_strategies.py`       | Strategy pattern (ExportAsJSON/Text)        |
| `test_user_service.py`            | Authentication logic, user roles            |
| `test_logger_singleton.py`        | Singleton behavior of LoggerService         |
| `test_notification_service.py`    | Email & SMS notifications                   |
| `test_ingredient_models.py`       | Ingredient subclasses (Vegetable, Fruit, …) |
| `test_abstract_recipe_service.py` | Abstract service contract                   |
---

## 📁 Project Structure

```plaintext
HealthyBiteApp/
├── app/
│   ├── __init__.py
│   ├── controllers.py
│   ├── models/
│   │   ├── recipe_models.py, user_models.py, ingredient_models.py
│   ├── services/
│   │   ├── concrete_recipe_service.py, recipe_factory.py, notification_service.py, ...
│   ├── strategies/
│   │   ├── export_strategy.py, export_as_text.py, export_as_json.py, recipe_exporter.py
│   ├── templates/
│   │   ├── index.html, add_recipe.html, meal_planner.html, shopping_list.html, ...
├── tests/
│   ├── test_recipe_service.py, test_export_strategies.py, ...
├── static/
├── instance/
├── run.py
├── requirements.txt
```
---

## 🚀 Installation & Run

✅ Requirements
- Python 3.10+
- Flask
- Flask SQLAlchemy

## 🛠️ Setup Instructions

git clone https://github.com/qhajdari/HealthyBiteApp.git
cd HealthyBiteApp
pip install -r requirements.txt
python -m flask --app run.py init-db
python run.py

Open browser at:
http://127.0.0.1:5000/

## 📄 License
This project is for academic and educational purposes.