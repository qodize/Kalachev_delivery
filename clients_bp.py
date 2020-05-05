from flask import Blueprint

blueprint = Blueprint('clients_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def client_login():
    pass
