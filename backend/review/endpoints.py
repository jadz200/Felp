from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import engine, get_db
from backend.review import crud, model
from backend.review.schema import Review as ReviewSchema

router = APIRouter(prefix="/review", tags=["Review"])

model.Base.metadata.create_all(bind=engine)


@router.get("/")
def get_all_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)


@router.get("/{restaurant_id}")
def get_review_restaurant(restaurant_id, db: Session = Depends(get_db)):
    db_reviews = crud.get_reviews_restaurant(db, restaurant_id)
    if db_reviews is None:
        raise HTTPException(status_code=404, detail="No reviews for this restaurant")
    return db_reviews


@router.post("/add")
def add_review(review: ReviewSchema, db: Session = Depends(get_db)):
    db_review = crud.add_review(db, review)
    return db_review
