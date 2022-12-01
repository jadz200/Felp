from sqlalchemy import Column, ForeignKey, Integer, String

from backend.database import Base


class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    text = Column(String)
    rating = Column(Integer)
