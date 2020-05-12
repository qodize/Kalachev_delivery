from flask import Blueprint
from login_required import login_required
from flask import Blueprint, render_template, redirect
from flask_login import current_user, logout_user
from main import login_user

from data import db_session
from data.users import User, WorkerData
from forms.worker_register_form import WorkerRegisterForm
from forms.worker_login_form import WorkerLoginForm

blueprint = Blueprint('admins_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = WorkerLoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        admin = session.query(User).filter(User.role == 'admin' and User.phone_number == form.phone_number.data).first()
        if admin and admin.check_password(form.password.data):
            login_user(admin, remember=True)
            return redirect('/admin/')
        return render_template(
            'worker_login.html',
            title='Авторизация',
            message='Неправильный логин или пароль',
            form=form
        )
    return render_template('worker_login.html', title='Авторизация', form=form)


@blueprint.route("/logout")
@login_required(role='admin')
def logout():
    logout_user()
    return redirect("/admin/login")

@blueprint.route('/', methods=['GET', 'POST'])
@login_required(role='admin')
def admin_home():
    return render_template('base_workers.html', title='Авторизация')


@blueprint.route('/register/<string:role>', methods=['GET', 'POST'])
@login_required(role='admin')
def register_worker(role: str):
    form = WorkerRegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        worker = session.query(User).filter(User.role == role and User.phone_number == form.phone_number.data).first()
        if worker:
            return render_template(
                'worker_registration.html',
                title='Регистрация',
                form=form,
                message='Работник с таким номером телефона уже зарегистрирован'
            )
        worker = User(
            name=form.name.data,
            surname=form.surname.data,
            phone_number=form.phone_number.data,
            email=form.email.data,
            birthday=form.birthday.data,
            role=role
        )
        worker_data = WorkerData(
            worker=worker,
            passport=form.passport.data,
            address=form.address.data
        )
        worker_data.set_password(form.password.data)
        session.add(worker)
        session.add(worker_data)
        session.commit()
        session.close()
        return redirect('/')
    return render_template('worker_registration.html', title='Регистрация', form=form)


@blueprint.route('/menu', methods=['GET', 'POST'])
@login_required(role='admin')
def menu():
    pass
