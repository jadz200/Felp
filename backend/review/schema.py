from pydantic import BaseModel, Field


class Review(BaseModel):
    user_id: int = Field()
    restaurant_id: int = Field()
    rating: int = Field()
    text: str = Field()
