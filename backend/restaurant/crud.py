from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.restaurant.model import Restaurant as RestaurantModel
from backend.restaurant.schema import Restaurant as RestaurantSchema


def get_restaurant(db: Session):
    return db.query(RestaurantModel).all()


def add_restaurants(db: Session, restaurant: RestaurantSchema):
    db_item = RestaurantModel(**restaurant.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_restaurant(db: Session, restaurant_id: int, restaurant: RestaurantSchema):
    db_item = get_restaurant_id(db, restaurant_id)

    if db_item is None:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    updated_data = restaurant.dict(exclude_unset=True)
    db.query(RestaurantModel).filter(restaurant_id == RestaurantModel.id).update(
        updated_data, synchronize_session=False
    )
    db.commit()

    return restaurant


def get_restaurant_id(db: Session, restaurant_id: int):
    return db.query(RestaurantModel).filter(restaurant_id == RestaurantModel.id).first()


def delete_restaurant(db: Session, restaurant_id: int):
    db_item = get_restaurant_id(db, restaurant_id)
    if db_item is None:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    db.delete(db_item)
    db.commit()
    db.close()
    return "Deleted"
