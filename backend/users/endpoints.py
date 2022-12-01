from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import engine, get_db
from backend.users import crud, model
from backend.users.schema import UserCredentials, UserSignUp

router = APIRouter(prefix="/user", tags=["User"])

model.Base.metadata.create_all(bind=engine)


@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.get("/{user_id}")
def read_restaurants(user_id, db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/sign_up")
def sign_up(user: UserSignUp, db: Session = Depends(get_db)):
    if user.confirm_password != user.password:
        return "password don't match"
    user_credentials = UserCredentials(email=user.email, password=user.password)
    return crud.add_user(db, user_credentials)


@router.post("/sign_in")
def sign_in(user: UserCredentials, db: Session = Depends(get_db)):

    db_user = crud.get_user_email(db, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.__dict__["password"] != user.password:
        raise HTTPException(status_code=400, detail="Wrong Password")
    return db_user
