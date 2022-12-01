from datetime import time

from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    name: str = Field()
    email: str = Field()
    phone: str = Field()
    opening: time = Field()
    closing: time = Field()
    rating: int = Field()
