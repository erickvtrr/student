from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('index.html')


@main_bp.route('./login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')


username_digitado = request.form.get('username')
flash(f'Tentativa de login com o usuário: {username_digitado}')


return redirect(url_for('main.login'))
# Handle login logic here
