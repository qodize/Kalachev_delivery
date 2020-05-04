import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = sa.Column(sa.String,
                     nullable=True)
    surname = sa.Column(sa.String,
                        nullable=True)
    phone_number = sa.Column(sa.String,
                             index=True,
                             unique=True,
                             nullable=True)
    email = sa.Column(sa.String,
                      index=True,
                      unique=True,
                      nullable=True)
    birthday = sa.Column(sa.String,
                         nullable=True)

    role = sa.Column(sa.String,
                     default='client')

    addresses = orm.relation("ClientAddress",
                             back_populates='client')

    client_orders = orm.relation("Order",
                                 back_populates='client')

    cook_orders = orm.relation("Order",
                               back_populates='cook')

    deliveryman_orders = orm.relation("Order",
                                      back_populates='deliveryman')

    worker_data = orm.relation("WorkerData",
                               back_populates='user')


class ClientAddress(SqlAlchemyBase):
    __tablename__ = 'client_addresses'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    data = sa.Column(sa.String, nullable=True)

    client = orm.relation("User")


class WorkerData(SqlAlchemyBase):
    __tablename__ = 'worker_data'

    worker_id = sa.Column(sa.Integer,
                          sa.ForeignKey('users.id'),
                          primary_key=True)

    passport = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)

    user = orm.relation('User')
