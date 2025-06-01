from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthybite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = 'super_secret_123'


    db.init_app(app) # registers the db with the Flask app

    from app import models  # register models to ensure they are created
    from app.controllers import register_routes
    register_routes(app)

    return app
