# app/routes.py

# 1. Importe TUDO o que vamos usar do Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for

# Cria o nosso conjunto de rotas
main_bp = Blueprint('main', __name__)


# Rota para a página inicial
@main_bp.route('/')
@main_bp.route('/index')
def index():
    # 2. Adicione o 'return' que estava faltando nesta função
    return render_template('index.html')


# Rota para a página de login
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Lida com o envio do formulário
    if request.method == 'POST':
        username_digitado = request.form.get('username')
        flash(f'Tentativa de login com o usuário: {username_digitado}')
        return redirect(url_for('main.login'))

    # Mostra a página de login se o método for GET
    return render_template('login.html')
