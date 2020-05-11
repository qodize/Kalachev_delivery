import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'categories'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    front_name = sa.Column(sa.String, nullable=True)
    back_name = sa.Column(sa.String, nullable=True)
    describtion = sa.Column(sa.String, nullable=True)

    products = orm.relation('Product',
                            back_populates='category',
                            foreign_keys='Product.category_id')
