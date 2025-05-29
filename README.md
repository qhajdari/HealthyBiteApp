# HealthyBiteApp

**HealthyBiteApp** is a web-based meal planning and recipe management application developed using **Python Flask**, following **Object-Oriented Programming (OOP)** principles and **MVC architecture**. It helps users plan healthy meals, manage recipes, and generate smart shopping lists based on weekly meal plans.

---

## 👨‍💻 

- **Project Name:** HealthyBite
- **Member:** Qendresa Hajdari

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
|----------------------------|-----------------------------------------------------|
| **Abstraction / Interface**| `AbstractRecipeService`, `ExportStrategy`, `User`   |
| **Inheritance (3 levels)** | `User → RegularUser → PremiumUser`                  |
| **Polymorphism**           | `get_role()` and `export()` methods                |
| **Exception Handling**     | `InvalidRecipeException`                            |
| **Enum**                   | `RecipeCategory`                                    |
| **Design Patterns**        | Factory, Singleton, Strategy                        |
| **Architecture**           | MVC (Model–View–Controller)                         |

---

## 📁 Project Structure

```plaintext
HealthyBiteApp/
├── app/
│   ├── __init__.py
│   ├── controllers.py
│   ├── models/
│   │   ├── recipe.py, meal_plan.py, user_models.py
│   ├── services/
│   │   ├── recipe_service.py, recipe_factory.py, exceptions.py
│   ├── strategies/
│   │   ├── export_strategy.py, export_as_text.py, export_as_json.py
│   ├── templates/
│   │   ├── index.html, add_recipe.html, meal_planner.html, ...
├── static/
├── instance/
├── run.py
├── requirements.txt
