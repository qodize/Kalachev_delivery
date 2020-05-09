from flask import Blueprint, redirect, render_template
from main import login_required, login_user
from forms.client_login_form import ClientLoginForm

from data import db_session
from data.users import User
from data.orders import Order

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


#  Авторизация
@blueprint.route('/login', methods=['GET', 'POST'])
def client_login():
    form = ClientLoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.role == 'client' and User.phone_number == form.phone_number.data).first()
        if user:
            login_user(user, remember=True)
            return redirect('/')
        user = User(
            phone_number=form.phone_number.data,
            role='client'
        )
        cart = Order(
            client=user
        )
        cart.update_total_cost()
        session.add(user)
        session.add(cart)
        session.commit()
        login_user(user, remember=True)
        return redirect('/')
    return render_template('client_login.html', title='Авторизация', form=form)


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
