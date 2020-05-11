from flask import Blueprint
from login_required import login_required
from flask import Blueprint, redirect, render_template
from flask_login import current_user, logout_user
from main import login_user

from data import db_session
from data.users import User
from forms.worker_login_form import WorkerLoginForm

blueprint = Blueprint('deliverymen_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def deliveryman_login():
    form = WorkerLoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.role == 'deliveryman' and
                                          User.phone_number == form.phone_number.data).first()
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
    pass
