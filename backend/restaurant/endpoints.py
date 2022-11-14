from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import engine, get_db
from backend.restaurant import crud, model
from backend.restaurant.schema import Restaurant as RestaurantSchema

router = APIRouter(prefix="/restaurant")

model.Base.metadata.create_all(bind=engine)


@router.get("/")
def read_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurant(db)


@router.get("/{restaurant_id}")
def read_restaurants(restaurant_id, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant_id(db, restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_restaurant


@router.post("/add")
def add_restaurant(restaurant: RestaurantSchema, db: Session = Depends(get_db)):
    return crud.add_restaurants(db, restaurant)


@router.put("/update/{restaurant_id}")
def update_restaurant(
    restaurant_id: int, restaurant: RestaurantSchema, db: Session = Depends(get_db)
):
    return crud.update_restaurant(db, restaurant_id, restaurant)


@router.delete("/delete/{restaurant_id}")
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return crud.delete_restaurant(db, restaurant_id)
