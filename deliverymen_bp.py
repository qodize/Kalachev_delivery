from flask import Blueprint
from login_required import login_required
from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, logout_user
from main import login_user

from data import db_session
from data.users import User
from data.orders import Order
from forms.worker_login_form import WorkerLoginForm

blueprint = Blueprint('deliverymen_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def deliveryman_login():
    form = WorkerLoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.role == 'deliveryman', User.phone_number == form.phone_number.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect('/deliveryman/')
        return render_template('worker_login.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('worker_login.html', title='Авторизация', form=form)


@blueprint.route("/logout")
@login_required(role='deliveryman')
def logout():
    logout_user()
    return redirect("/deliveryman/login")


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/orders', methods=['GET', 'POST'])
@login_required(role='deliveryman')
def deliveryman_orders():
    session = db_session.create_session()
    new_orders = session.query(Order).filter(Order.status == 3).all()
    delivering_orders = session.query(Order).filter(Order.status == 4, Order.deliveryman_id == current_user.id).all()
    done_orders = session.query(Order).filter(Order.status == 5, Order.deliveryman_id == current_user.id).all()
    if request.method == 'POST':
        req_form = dict(request.form)
        if req_form['act'] == 'accept order':
            order_id = req_form['order_id']
            order = session.query(Order).get(order_id)
            if order.status == 3:
                deliveryman = session.query(User).get(current_user.id)
                order.increase_status(deliveryman=deliveryman)
                session.merge(order)
                session.commit()
            return redirect('/deliveryman/orders')
        elif req_form['act'] == 'order done':
            order_id = req_form['order_id']
            order = session.query(Order).get(order_id)
            order.increase_status()
            session.merge(order)
            session.commit()
            return redirect('/deliveryman/orders')

    return render_template('deliveryman_orders.html', title='Заказы',
                           new_orders=new_orders,
                           delivering_orders=delivering_orders,
                           done_orders=done_orders)
