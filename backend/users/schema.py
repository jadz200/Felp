from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str = Field()
    email: str = Field()
    gender: str = Field()
    age: int = Field()
    bio: str = Field()


class UserSignUp(BaseModel):
    email: str = Field()
    password: str = Field()
    confirm_password: str = Field()


class UserCredentials(BaseModel):
    email: str = Field()
    password: str = Field()
