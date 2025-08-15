# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from pathlib import Path  # Importe a biblioteca Path

# --- INÍCIO DA MODIFICAÇÃO ---

# Encontra o caminho para a pasta principal do projeto (um nível acima da pasta 'app')
BASE_DIR = Path(__file__).resolve().parent.parent

# Constrói o caminho completo para o arquivo .env
dotenv_path = BASE_DIR / '.env'

# Carrega o arquivo .env a partir do caminho que especificamos
load_dotenv(dotenv_path=dotenv_path)

# --- FIM DA MODIFICAÇÃO ---


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Agora o os.getenv() vai funcionar porque o load_dotenv encontrou o arquivo
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        raise ValueError(
            "A variável DATABASE_URL não foi encontrada. Verifique seu arquivo .env")

    app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # O resto do seu código permanece igual...
    from .routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        from . import models
        db.create_all()

    return app
