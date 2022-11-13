from sqlalchemy import Column, Integer, String,TIME
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.database import Base

class Restaurant(Base):
    __tablename__ = "restaurant"
    
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    phone=Column(String)
    opening=Column(TIME)
    closing=Column(TIME)
    rating=Column(Integer)