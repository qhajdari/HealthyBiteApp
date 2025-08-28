# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_overrides: dict | None = None):
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)

    # default DB: instance/healthybite.db
    db_path = os.path.join(app.instance_path, "healthybite.db")
    db_uri = "sqlite:///" + db_path.replace("\\", "/")

    app.config.update(
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY="dev",
        REGISTER_ROUTES=True,
        TESTING=False,
    )

    # prano overrides nga teste ose run.py
    if config_overrides:
        app.config.update(config_overrides)

    # init DB pasi config u vendos
    db.init_app(app)

    # register routes
    if app.config.get("REGISTER_ROUTES", True):
        from app.controllers import register_routes
        register_routes(app)

    # lidhet me UI - context_processor per rol/meny
    @app.context_processor
    def inject_user():
        from flask import session
        return {
            "current_user": session.get("user"),
            "current_role": session.get("role"),
            "is_logged_in": "user" in session,
            "is_admin": session.get("role") == "Admin",
            "is_premium": session.get("role") == "Premium",
            "is_regular": session.get("role") == "Regular",
        }

    return app
