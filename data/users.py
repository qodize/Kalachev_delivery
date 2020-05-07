import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


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
                             back_populates='client',
                             foreign_keys='ClientAddress.client_id')

    client_orders = orm.relation("Order",
                                 back_populates='client',
                                 foreign_keys='Order.client_id')

    cook_orders = orm.relation("Order",
                               back_populates='cook',
                               foreign_keys='Order.cook_id')

    deliveryman_orders = orm.relation("Order",
                                      back_populates='deliveryman',
                                      foreign_keys='Order.deliveryman_id')

    worker_data = orm.relation("WorkerData",
                               back_populates='worker',
                               foreign_keys='WorkerData.worker_id',
                               uselist=False)

    def set_password(self, pwd: str) -> None:
        if self.worker_data:
            self.worker_data.set_password(pwd)

    def check_password(self, pwd: str) -> bool:
        if self.worker_data:
            return self.worker_data.check_password(pwd)
        return False


class ClientAddress(SqlAlchemyBase):
    __tablename__ = 'client_addresses'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    data = sa.Column(sa.String, nullable=True)

    client = orm.relation("User", foreign_keys=[client_id])


class WorkerData(SqlAlchemyBase):
    __tablename__ = 'worker_data'

    worker_id = sa.Column(sa.Integer,
                          sa.ForeignKey('users.id'),
                          primary_key=True)

    passport = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)

    worker = orm.relation('User', foreign_keys=[worker_id])

    def set_password(self, pwd: str) -> None:
        self.hashed_password = generate_password_hash(pwd)

    def check_password(self, pwd: str) -> bool:
        return check_password_hash(self.hashed_password, pwd)
