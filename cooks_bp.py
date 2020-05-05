from flask import Blueprint

blueprint = Blueprint('cooks_bp', __name__,
                      template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def cook_login():
    pass
