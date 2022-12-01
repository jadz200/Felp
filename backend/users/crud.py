from sqlalchemy.orm import Session

from backend.users.model import User as UserModel
from backend.users.schema import UserCredentials


def get_users(db: Session):
    return db.query(UserModel).all()


def add_user(db: Session, user: UserCredentials):
    db_item = UserModel(**user.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_id(db: Session, user_id: int):
    return db.query(UserModel).filter(user_id == UserModel.id).first()


def get_user_email(db: Session, email: str):
    return db.query(UserModel).filter(email == UserModel.email).first()
