from flask import Flask
from data import db_session
from flask_login import LoginManager, current_user
from functools import wraps

from data.users import User, ClientAddress, WorkerData
from data.orders import Order
from data.products import Product
from data.positions import Position


global_session = db_session.create_session()
client = User(
    id=0,
    name='Cl',
    surname='aa',
    phone_number='898',
    email='apokd',
    birthday='12.12.12',
)
address = ClientAddress(
    id=0,
    data='asd',
    client=client
)
global_session.add(client)
global_session.add(address)
global_session.commit()

cook = User(
    id=1,
    name='Karl',
    surname='aaa',
    phone_number='9999',
    email='asdasd',
    birthday='11.11.11'
)
worker_data = WorkerData(
    worker_id=1,
    passport='8017',
    address='Pushkina dom kalatuchkina'
)
cook.set_password('121321')
global_session.add(cook)
global_session.add(worker_data)
global_session.commit()

order = Order(
    id=0,
    client_id=0,
    address_data="no",
)

product = Product(
    id=0,
    back_name='aaa',
    front_name='Aaa',
    description='sadsaas',
    ingredients='1, 2, 3',
    cost=100
)
global_session.add(order)
global_session.add(product)
global_session.commit()
position = Position(
    order=order,
    product=product,
    count=2,
    extra_wishes='asd',
    point_cost=product.cost * 2
)
global_session.add(position)
global_session.commit()
print(order.positions)
print(product in order)
print(order.status)
order.increase_status()
global_session.merge(order)
global_session.commit()
print(order.status)
order.increase_status(cook=cook)
global_session.merge(order)
global_session.commit()
print(order.status)
print(order.cook)
print(product in order)
