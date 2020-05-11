import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase, create_session
from .products import Product
# from .positions import Position


class Order(SqlAlchemyBase):
    __tablename__ = 'orders'

    statuses = ['basket', 'wait for cook', 'cooking',
                'wait for delivery', 'delivering', 'finished']

    id = sa.Column(sa.Integer,
                   primary_key=True,
                   autoincrement=True)
    client_id = sa.Column(sa.Integer,
                          sa.ForeignKey("users.id"),
                          nullable=True)
    cook_id = sa.Column(sa.Integer,
                        sa.ForeignKey("users.id"),
                        nullable=True)
    deliveryman_id = sa.Column(sa.Integer,
                               sa.ForeignKey("users.id"),
                               nullable=True)
    address_data = sa.Column(sa.String,
                             nullable=True)
    delivery_time = sa.Column(sa.String,
                              nullable=True)
    payment_way = sa.Column(sa.String,
                            nullable=True)
    short_change = sa.Column(sa.Integer,
                             nullable=True)
    commentary = sa.Column(sa.String,
                           nullable=True)
    order_date = sa.Column(sa.Date,
                           nullable=True)
    status = sa.Column(sa.Integer,
                       default=0)
    total_cost = sa.Column(sa.Integer,
                           nullable=True)

    client = orm.relation('User', foreign_keys=[client_id])
    cook = orm.relation('User', foreign_keys=[cook_id])
    deliveryman = orm.relation('User', foreign_keys=[deliveryman_id])

    positions = orm.relation('Position',
                             back_populates='order',
                             foreign_keys='Position.order_id')

    #  принимает в качестве cook и deliveryman объекты классов
    #  Cook и DeliveryMan
    def increase_status(self, cook=None, deliveryman=None):
        #  Проверяю, указаны ли повар и доставщик
        #  Если заказ принят поваром
        if self.status == 1:
            if not cook:
                return {'failure': 'Не указан повар'}
            self.cook_id = cook.id
            self.cook = cook
        #  Если заказ принят доставщиком
        if self.status == 3:
            if not deliveryman:
                return {'failure': 'Не указан доставщик'}
            self.deliveryman_id = deliveryman.id
            self.deliveryman = deliveryman
        #  Во всех остальных случаях достаточно только прибавить статус
        self.status += 1
        return {'success': 'OK'}

    #  переопределил оператор чтобы можно было смело использовать что-то типо
    #  if product in order:
    #      print(f'Да, в заказе {order} есть продукт {product}')
    def __contains__(self, product: Product) -> bool:
        return product.id in [position.product_id for position in self.positions]

    def update_total_cost(self) -> None:
        total_cost = sum(map(lambda item: item.point_cost, self.positions))
        self.total_cost = total_cost

    #  добавить продукт в заказ (при передаче объекта класса Product)
    #  (Она не работает поэтому закомментил
    # def add_product(self, product_id: int, count=1, extra_wishes=None) -> None:
    #     session = create_session()
    #     product = session.query(Product).get(product_id)
    #     position = Position(
    #         order=self,
    #         product=product,
    #         count=count,
    #         extra_wishes=extra_wishes,
    #         point_cost=product.cost * count
    #     )
    #     session.add(position)
    #     session.commit()
    #     session.close()
