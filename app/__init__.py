# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # 1. Busca a variável 'DATABASE_URL' do ambiente
    database_url = os.getenv(
        'postgresql://postgres.altajzefwnzacajefaix:pg@atualDev@aws-1-sa-east-1.pooler.supabase.com:5432/postgres')

    # 2. Verifica se a variável foi encontrada
    if not database_url:
        raise ValueError(
            "A variável DATABASE_URL não foi encontrada. Verifique seu arquivo .env")

    # 3. Configura o aplicativo Flask com a URL carregada
    app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registra as rotas (blueprints)
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Cria as tabelas do banco de dados, se não existirem
    with app.app_context():
        from . import models  # Certifique-se de que seus modelos estão sendo importados
        db.create_all()

    return app
