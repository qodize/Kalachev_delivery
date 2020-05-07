import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Position(SqlAlchemyBase):
    __tablename__ = 'positions'

    id = sa.Column(sa.Integer, primary_key=True,
                   autoincrement=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'),
                           nullable=True)
    count = sa.Column(sa.Integer, nullable=True)
    extra_wishes = sa.Column(sa.String, nullable=True)
    point_cost = sa.Column(sa.Integer, nullable=True)

    order = orm.relation('Order')
    product = orm.relation('Product')
