from flask import Blueprint
from login_required import login_required

blueprint = Blueprint('admins_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    pass


@blueprint.route('/register_cook', methods=['GET', 'POST'])
@login_required(role='admin')
def register_cook():
    pass


@blueprint.route('/register_deliveryman', methods=['GET', 'POST'])
@login_required(role='admin')
def register_deliveryman():
    pass


@blueprint.route('/menu', methods=['GET', 'POST'])
@login_required(role='admin')
def menu():
    pass
