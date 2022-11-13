from sqlalchemy.orm import Session
from backend.models.restaurant import Restaurant as RestaurantModel 
from backend.schema.restaurant import Restaurant as RestaurantSchema

def get_restaurant(db: Session):
    return db.query(RestaurantModel).all()

def add_restaurants(db: Session,restaurant:RestaurantSchema):
    db_item=RestaurantModel(**restaurant.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_restaurant_id(db:Session, restaurant_id:int):
    return db.query(RestaurantModel).filter(restaurant_id==RestaurantModel.id).first()