from flask import Flask, redirect
from data import db_session
from flask_login import LoginManager, current_user, login_user
from functools import wraps

from data.users import User, ClientAddress, WorkerData
from data.orders import Order
from data.products import Product
from data.positions import Position


import admins_bp
import clients_bp
import cooks_bp
import deliverymen_bp
import tests_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = '54321qwerty'

login_manager = LoginManager()
login_manager.init_app(app)


#  Вместо декоратора из библиотеки нам понадобится свой, т.к. у нас несколько ролей
#  Сам я взял этот декоратор с какого-то треда на каком-то сайте
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                # return login_manager.unauthorized()
                if role == 'client':
                    return redirect('/login')
                return redirect(f'/{role}/login')
            if not (current_user.role == role or role == "ANY"):
                # return login_manager.unauthorized()
                if role == 'client':
                    return redirect('/login')
                return redirect(f'/{role}/login')
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


def main():
    db_session.global_init('db/PizzaMan_db.db')

    # app.register_blueprint(tests_bp.blueprint, url_prefix='/tests')
    app.register_blueprint(admins_bp.blueprint, url_prefix='/admin')
    app.register_blueprint(clients_bp.blueprint)
    app.register_blueprint(cooks_bp.blueprint, url_prefix='/cook')
    app.register_blueprint(deliverymen_bp.blueprint, url_prefix='/deliveryman')

    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
