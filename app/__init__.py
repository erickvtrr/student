# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    database_url = os.getenv(
        'postgresql://postgres:[pg@atualDev]@db.altajzefwnzacajefaix.supabase.co:5432/postgres')
    if not database_url:
        raise ValueError(
            "DATABASE_URL não encontrada no arquivo .env. Verifique o arquivo.")

    app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        from . import models
        db.create_all()

    return app
