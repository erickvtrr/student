import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():

    app = flask(__name__)

    app.config['es'] = os.getenv('es'), ('erick.silva')

    app.config['SQLACHEMY_DATABASE_URI'] = os.getenv(
        'postgresql://postgres:[1234]@db.altajzefwnzacajefaix.supabase.co:5432/postgres')
    app.config['SQLALCHEMY_TREACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    return app
