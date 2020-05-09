from flask import Blueprint, render_template
from client_form import ClientForm
from address_form import AddressForm
from data.users import User
from data import db_session
from flask import Blueprint
from main import login_required

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


#  Авторизация
@blueprint.route('/login', methods=['GET', 'POST'])
def client_login():
    return render_template('login.html', title='Авторизация')

  
# Главная
@blueprint.route('/', methods=['GET'])
def index():
    return render_template('home.html', title='Главная')

  
#  ЛК
@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required(role='client')
def profile():
    form = ClientForm()
    form_address = AddressForm()
    # if form.validate_on_submit():
    #     session = db_session.create_session()
    #     if session.query(User).filter(User.email == form.email.data).first():
    #         return render_template(
    #             "profile.html",
    #             title='Профиль',
    #             form_modal_edit=form,
    #             message='Пользователь с таким email уже существует.'
    #         )
    # я не панимаю, но здесь должно быть что-то вроде этого

    return render_template('profile.html', title='Профиль', form_modal_edit=form, form_address=form_address)


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




