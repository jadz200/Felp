from sqlalchemy import TIME, Column, Integer, String

from backend.database import Base


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    opening = Column(TIME)
    closing = Column(TIME)
    rating = Column(Integer)
