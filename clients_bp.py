from flask import Blueprint, render_template, redirect
from forms.client_form import ClientForm
from forms.address_form import AddressForm
from login_required import login_required
from flask_login import current_user, logout_user
from main import login_user
from forms.client_login_form import ClientLoginForm

from data import db_session
from data.users import User, ClientAddress
from data.orders import Order

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


#  Авторизация
@blueprint.route('/login/', methods=['GET', 'POST'])
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
    return render_template('login.html', title='Авторизация', form=form)


@blueprint.route("/logout")
@login_required(role='client')
def logout():
    logout_user()
    return redirect("/")


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
    session = db_session.create_session()
    user = session.query(User).filter(User.id == current_user.id).first()
    if form.validate_on_submit():
        user.name = form.name.data
        user.surname = form.surname.data
        user.email = form.email.data
        user.birthday = '.'.join([form.day.data, form.month.data, form.year.data])
        session.merge(user)
        session.commit()
    if form_address.validate_on_submit():
        address = ClientAddress(
            client=user,
            data=f'г.{form_address.city.data}, ул. {form_address.street.data}, д. {form_address.house_number.data}, ' +
            f'кв. {form_address.flat.data}, подъезд {form_address.entrance.data}, этаж {form_address.floor.data}, ' +
            f'код домофона {form_address.doorphone.data}'
        )
        session.add(address)
        session.commit()
    user.client_orders = list(reversed(user.client_orders))
    return render_template('profile.html', title='Профиль', form_modal_edit=form,
                           form_address=form_address, current_user=user)


#  Корзина
@blueprint.route('/basket', methods=['GET', 'POST'])
@login_required(role='client')
def basket():
    return render_template('basket.html', title='Корзина')


#  Создание заказа
@blueprint.route('/checkout', methods=['GET', 'POST'])
@login_required(role='client')
def checkout():
    pass


@blueprint.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html', title='Меню')

# @blueprint.route('/product/<int:product_id>', methods=['GET', 'POST'])
@blueprint.route('/product', methods=['GET', 'POST'])
def products():
    product_title = 'Название товара'
    return render_template('product.html', product_title=product_title)

