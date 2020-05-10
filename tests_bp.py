from flask import Blueprint
from main import login_user
from login_required import login_required
from data.db_session import create_session
from data.users import User

blueprint = Blueprint('tests_bp', __name__,
                      template_folder='templates')


@blueprint.route('/admin_login', methods=['GET'])
def admin_login():
    user = User(
        name='admin',
        role='admin'
    )
    session = create_session()
    session.add(user)
    session.commit()
    login_user(user)
    session.close()
    return 'ok'


@blueprint.route('/client_login', methods=['GET'])
def client_login():
    user = User(
        name='client',
        role='client'
    )
    session = create_session()
    session.add(user)
    session.commit()
    login_user(user)
    session.close()
    return 'ok'


@blueprint.route('/cook_login', methods=['GET'])
def cook_login():
    user = User(
        name='cook',
        role='cook'
    )
    session = create_session()
    session.add(user)
    session.commit()
    login_user(user)
    session.close()
    return 'ok'


@blueprint.route('/deliveryman_login', methods=['GET'])
def deliveryman_login():
    user = User(
        name='deliveryman',
        role='deliveryman'
    )
    session = create_session()
    session.add(user)
    session.commit()
    login_user(user)
    session.close()
    return 'ok'


@blueprint.route('/admin_test', methods=['GET'])
@login_required(role='admin')
def admin_test():
    return 'OK u are admin'


@blueprint.route('/deliveryman_test', methods=['GET'])
@login_required(role='deliveryman')
def deliveryman_test():
    return 'OK u are deliveryman'


@blueprint.route('/cook_test', methods=['GET'])
@login_required(role='cook')
def cook_test():
    return 'OK u are cook'


@blueprint.route('/client_test', methods=['GET'])
@login_required(role='client')
def client_test():
    return 'OK u are client'


