import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    back_name = sa.Column(sa.String,
                          nullable=True)
    front_name = sa.Column(sa.String,
                           nullable=True)
    description = sa.Column(sa.String,
                            nullable=True)
    ingredients = sa.Column(sa.String,
                            nullable=True)
    cost = sa.Column(sa.Integer,
                     nullable=True)
