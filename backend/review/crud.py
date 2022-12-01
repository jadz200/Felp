from sqlalchemy.orm import Session

from backend.review.model import Review as ReviewModel
from backend.review.schema import Review as ReviewSchema


def get_reviews(db: Session):
    return db.query(ReviewModel).all()


def add_review(db: Session, review: ReviewSchema):
    db_item = ReviewModel(**review.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_reviews_restaurant(db: Session, restaurant_id: int):
    return (
        db.query(ReviewModel).filter(restaurant_id == ReviewModel.restaurant_id).all()
    )
