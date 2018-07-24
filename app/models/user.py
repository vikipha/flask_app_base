from typing import Optional

from sqlalchemy import Column, Integer, String
from models.base import Base
from core.database import db_session


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)

    @property
    def full_name(self):
        # type: () -> str
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        # type: () -> str
        return "<User(name='{}', id={})>".format(
            self.full_name, self.id
        )

    @staticmethod
    def find_by_credentials(login, password):
        # type: (str, str) -> Optional[User]
        return db_session.query(User).filter(
            User.login == login,
            User.password == password
        ).first()
