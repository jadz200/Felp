from sqlalchemy import Column, Integer, String

from backend.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    email = Column(String, unique=True)
    password = Column(String)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    bio = Column(String, nullable=True)
