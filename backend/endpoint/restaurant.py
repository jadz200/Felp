from http.client import HTTPException
from fastapi import APIRouter, Depends
from backend.database import engine, get_db
from sqlalchemy.orm import Session
from backend.models import restaurant
from backend.schema.restaurant import Restaurant as  RestaurantSchema
from backend.crud import restaurants
router = APIRouter(prefix="/restaurant")

restaurant.Base.metadata.create_all(bind=engine)



@router.get("/")
def read_restaurants(db: Session = Depends(get_db)):
    return restaurants.get_restaurant(db)

@router.get("/{restaurant_id}")
def read_restaurants(restaurant_id,db: Session = Depends(get_db)):
    db_restaurant = restaurants.get_restaurant_id(db,restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_restaurant

@router.post("/add")
def add_restaurant(restaurant:RestaurantSchema,db: Session = Depends(get_db)):
    return restaurants.add_restaurants(db, restaurant)
