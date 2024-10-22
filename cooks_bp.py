from flask import Blueprint
from login_required import login_required
from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, logout_user
from main import login_user
from forms.worker_login_form import WorkerLoginForm

from data import db_session
from data.users import User
from data.orders import Order

blueprint = Blueprint('cooks_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def cook_login():
    form = WorkerLoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.role == 'cook', User.phone_number == form.phone_number.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect('/cook/orders')
        return render_template('worker_login.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('worker_login.html', title='Авторизация', form=form)


@blueprint.route("/logout")
@login_required(role='cook')
def logout():
    logout_user()
    return redirect("/cook/login")


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/orders', methods=['GET', 'POST'])
@login_required(role='cook')
def cook_orders():
    session = db_session.create_session()
    new_orders = session.query(Order).filter(Order.status == 1).all()
    cooking_orders = session.query(Order).filter(Order.status == 2, Order.cook_id == current_user.id).all()
    done_orders = session.query(Order).filter(Order.status > 2, Order.cook_id == current_user.id).all()
    if request.method == 'POST':
        req_form = dict(request.form)
        if req_form['act'] == 'accept order':
            order_id = req_form['order_id']
            order = session.query(Order).get(order_id)
            if order.status == 1:
                cook = session.query(User).get(current_user.id)
                order.increase_status(cook)
                session.merge(order)
                session.commit()
            return redirect('/cook/orders')
        elif req_form['act'] == 'order done':
            order_id = req_form['order_id']
            order = session.query(Order).get(order_id)
            order.increase_status()
            session.merge(order)
            session.commit()
            return redirect('/cook/orders')
    return render_template('cook_orders.html', title='Заказы',
                           new_orders=new_orders, cooking_orders=cooking_orders,
                           done_orders=done_orders)
