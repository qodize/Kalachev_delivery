from flask import Blueprint, render_template, redirect, request
from forms.client_form import ClientForm
from forms.address_form import AddressForm
from login_required import login_required
from flask_login import current_user, logout_user
from main import login_user

from forms.client_login_form import ClientLoginForm

from data import db_session
from data.users import User, ClientAddress
from data.orders import Order
from data.positions import Position
from data.products import Product
from data.categories import Category


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
    session = db_session.create_session()
    user = session.query(User).filter(User.id == current_user.id).first()
    basket = session.query(Order).filter(Order.client_id == user.id, Order.status == 0).first()
    if request.method == 'POST':
        req_form = dict(request.form)
        if req_form['act'] == 'up':
            position = session.query(Position).filter(Position.id == int(req_form['position_id'])).first()
            position.count += 1
            position.update_point_cost()
            session.merge(position)
            session.commit()
        elif req_form['act'] == 'down':
            position = session.query(Position).filter(Position.id == int(req_form['position_id'])).first()
            position.count = max(0, position.count - 1)
            position.update_point_cost()
            session.merge(position)
            if position.count == 0:
                session.delete(position)
            session.commit()
        elif req_form['act'] == 'delete':
            position = session.query(Position).filter(Position.id == int(req_form['position_id'])).first()
            session.delete(position)
            session.commit()
        elif req_form['act'] == 'do order':
            basket.status += 1
            session.merge(basket)
            session.commit()
        return redirect('/basket')
    return render_template('basket.html', title='Корзина', current_user=user, basket=basket)


#  Создание заказа
@blueprint.route('/checkout', methods=['GET', 'POST'])
@login_required(role='client')
def checkout():
    pass


@blueprint.route('/menu', methods=['GET', 'POST'])
def menu():
    session = db_session.create_session()
    categories = session.query(Category).all()
    if request.method == 'POST':
        product_id = int(dict(request.form)['product_id'])
        product = session.query(Product).filter(Product.id == product_id).first()
        order = session.query(Order).filter(Order.client_id == current_user.id and Order.status == 0).first()
        if not order:
            order = Order(
                client_id=current_user.id,
                status=0,
                total_cost=0
            )
            session.add(order)
            session.commit()
        if product in order:
            position = session.query(Position).filter(Position.order_id == order.id and Position.product_id == product_id).first()
            position.count += 1
            position.update_point_cost()
            session.merge(position)
            session.commit()
        else:
            position = Position(
                order=order,
                product=product,
                count=1
            )
            position.update_point_cost()
            session.add(position)
            session.commit()
        return redirect('/menu')
    return render_template('menu.html', title='Меню', categories=categories)


# @blueprint.route('/product/<int:product_id>', methods=['GET', 'POST'])
@blueprint.route('/product', methods=['GET', 'POST'])
def products():
    product_title = 'Название товара'
    return render_template('product.html', product_title=product_title)

