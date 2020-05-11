from flask import Flask, redirect
from data import db_session
from flask_login import LoginManager, current_user, login_user
from functools import wraps
from login_required import login_required

from data.users import User, ClientAddress, WorkerData
from data.orders import Order
from data.products import Product
from data.positions import Position
from data.categories import Category

import admins_bp
import clients_bp
import cooks_bp
import deliverymen_bp
import tests_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = '54321qwerty'

login_manager = LoginManager()
login_manager.init_app(app)


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

    session = db_session.create_session()
    category1 = Category(
        front_name='Большая пицца',
        back_name='big-pizza',
        describtion='aasd'
    )
    category2 = Category(
        front_name='Маленькая пицца',
        back_name='small-pizza',
        describtion='qqwe'
    )
    product1 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Первая большая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category1
    )
    product2 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Вторая большая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=140,
        category=category1
    )
    product3 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Третья большая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=100,
        category=category1
    )
    product4 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Четвертая большая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category1
    )
    product5 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Первая маленькая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category2
    )
    product6 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Вторая маленькая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category2
    )
    product7 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Третья маленькая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category2
    )
    product8 = Product(
        back_name='zakIardbo_Q.jpg',
        front_name='Четвертая маленькая пицца',
        description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
        cost=130,
        category=category2
    )
    session.add(category1)
    session.add(category2)
    session.add(product1)
    session.add(product2)
    session.add(product3)
    session.add(product4)
    session.add(product5)
    session.add(product6)
    session.add(product7)
    session.add(product8)
    session.commit()
    session.close()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
