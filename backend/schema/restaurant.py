from pydantic import BaseModel, Field
from uuid import UUID
from datetime import time

class Restaurant(BaseModel):
    id: int
    name: str =Field()
    email: str =Field()
    phone: str =Field()
    opening: time =Field()
    closing: time =Field()
    rating:  int =Field()