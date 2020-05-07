import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


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
                               sa.ForeignKey('users.id'),
                               nullable=True)
    address_data = sa.Column(sa.String,
                             nullable=True)
    delivery_time = sa.Column(sa.String,
                              nullable=True)
    status = sa.Column(sa.Integer,
                       nullable=True)
    total_cost = sa.Column(sa.Integer,
                           nullable=True)

    client = orm.relation('User')
    cook = orm.relation('User')
    deliveryman = orm.relation('User')

    positions = orm.relation('Position',
                             back_populates='order')

    #  принимает в качестве cook и deliveryman объекты классов
    #  Cook и DeliveryMan
    def increase_status(self, cook=None, deliveryman=None):
        #  Проверяю, указаны ли повар и доставщик
        #  Если заказ принят поваром
        if self.status == 1:
            if not cook:
                return {'failure': 'Не указан повар'}
            self.cook_id = cook.id
        #  Если заказ принят доставщиком
        if self.status == 3:
            if not deliveryman:
                return {'failure': 'Не указан доставщик'}
        #  Во всех остальных случаях достаточно только прибавить статус
        self.status += 1
        return {'success': 'OK'}
