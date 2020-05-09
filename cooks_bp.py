from flask import Blueprint
from login_required import login_required

blueprint = Blueprint('cooks_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def cook_login():
    pass


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/orders', methods=['GET', 'POST'])
@login_required(role='cook')
def cook_orders():
    pass
