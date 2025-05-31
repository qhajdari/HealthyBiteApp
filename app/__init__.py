from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # ← kjo duhet të jetë e vetmja instancë

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthybite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = 'super_secret_123'


    db.init_app(app)  # ← ky hap është i domosdoshëm

    from app import models  # regjistron modelet që përdorin db.Model
    from app.controllers import register_routes
    register_routes(app)

    return app
