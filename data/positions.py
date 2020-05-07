import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Position(SqlAlchemyBase):
    __tablename__ = 'positions'

    id = sa.Column(sa.Integer, primary_key=True,
                   autoincrement=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'),
                         nullable=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'),
                           nullable=True)
    count = sa.Column(sa.Integer, nullable=True)
    extra_wishes = sa.Column(sa.String, nullable=True)
    point_cost = sa.Column(sa.Integer, nullable=True)

    order = orm.relation('Order', foreign_keys=[order_id])
    product = orm.relation('Product', foreign_keys=[product_id])
