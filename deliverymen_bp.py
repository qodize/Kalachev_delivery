from flask import Blueprint
from login_required import login_required

blueprint = Blueprint('deliverymen_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def deliveryman_login():
    pass


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/orders', methods=['GET', 'POST'])
@login_required(role='client')
def deliveryman_orders():
    pass
