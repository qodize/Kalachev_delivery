from flask import Blueprint, render_template

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def client_login():
    return render_template('login.html', title='Авторизация')


@blueprint.route('/', methods=['GET', 'POST'])
def client_home():
    return render_template('home.html', title='Главная')


@blueprint.route('/profile')
def profile():
    return render_template('profile.html', title='Профиль')
