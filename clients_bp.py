from flask import Blueprint, render_template
from client_form import ClientForm
from address_form import AddressForm
from data.users import User
from data import db_session

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
