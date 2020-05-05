from flask import Blueprint

blueprint = Blueprint('deliverymen_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def deliveryman_login():
    pass
