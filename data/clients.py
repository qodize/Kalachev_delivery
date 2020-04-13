import sqlalchemy as sa
from sqlalchemy import orm
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase, UserMixin):
    __tablename__ = 'clients'

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
    birthday = sa.Column(sa.Date,
                         nullable=True)
    
    addresses = orm.relation("ClientAddress",
                             back_populates='client')

    orders = orm.relation("Order",
                          back_populates='client')


class ClientAddress(SqlAlchemyBase):
    __tablename__ = 'client_addresses'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey("clients.id"))
    data = sa.Column(sa.String, nullable=True)

    client = orm.relation("Client")
