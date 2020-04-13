import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


order_to_product_table = sa.Table(
    'order_to_product', SqlAlchemyBase.metadata,
    sa.Column('order', sa.Integer,
              sa.ForeignKey('orders.id')),
    sa.Column('product', sa.Integer,
              sa.ForeignKey('products.id'))
)


class Order(SqlAlchemyBase):
    __tablename__ = 'orders'

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    client_id = sa.Column(sa.Integer,
                          sa.ForeignKey("clients.id"),
                          nullable=True)
    cook_id = sa.Column(sa.Integer,
                        sa.ForeignKey("cooks.id"),
                        nullable=True)
    deliveryman_id = sa.Column(sa.Integer,
                               sa.ForeignKey('deliverymen.id'),
                               nullable=True)
    address_data = sa.Column(sa.String,
                             nullable=True)
    delivery_time = sa.Column(sa.DateTime,
                              nullable=True)
    status = sa.Column(sa.String,
                       nullable=True)
    total_cost = sa.Column(sa.Integer,
                           nullable=True)

    client = orm.relation('Client')
    cook = orm.relation('Cook')
    deliveryman = orm.relation('Deliveryman')

    products = orm.relation('Product',
                            secondary='order_to_product',
                            backref='order')
