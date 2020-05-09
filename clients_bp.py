from flask import Blueprint
from main import login_required

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


#  Авторизация
@blueprint.route('/login', methods=['GET', 'POST'])
def client_login():
    pass


#  ЛК
@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required(role='client')
def profile():
    pass


#  Корзина
@blueprint.route('/cart', methods=['GET', 'POST'])
@login_required(role='client')
def cart():
    pass


#  Создание заказа
@blueprint.route('/checkout', methods=['GET', 'POST'])
@login_required(role='client')
def checkout():
    pass


@blueprint.route('/menu', methods=['GET', 'POST'])
def menu():
    pass


@blueprint.route('/', methods=['GET'])
def index():
    pass
