from datetime import time
from uuid import UUID

from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    id: int
    name: str = Field()
    email: str = Field()
    phone: str = Field()
    opening: time = Field()
    closing: time = Field()
    rating: int = Field()
