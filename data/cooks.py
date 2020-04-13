import sqlalchemy as sa
from sqlalchemy import orm
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Cook(SqlAlchemyBase, UserMixin):
    __tablename__ = 'cooks'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = sa.Column(sa.String,
                     nullable=True)
    surname = sa.Column(sa.String,
                        nullable=True)
    father_name = sa.Column(sa.String,
                            nullable=True)
    birthday = sa.Column(sa.Date,
                         nullable=True)
    phone_number = sa.Column(sa.String,
                             index=True,
                             unique=True,
                             nullable=True)
    passport = sa.Column(sa.String,
                         nullable=True)
    hashed_password = sa.Column(sa.String,
                                nullable=True)
    address = sa.Column(sa.String,
                        nullable=True)

    orders = orm.relation("Order",
                          back_populates='cook')
