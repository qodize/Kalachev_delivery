import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(SqlAlchemyBase):
    __tablename__ = 'admins'

    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.String, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)

    def set_password(self, password: str) -> None:
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.hashed_password, password)
