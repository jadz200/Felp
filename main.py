from fastapi import FastAPI

from backend.restaurant.endpoints import router as restaurant_router
from backend.review.endpoints import router as review_router
from backend.users.endpoints import router as user_router

app = FastAPI()


app.include_router(restaurant_router)
app.include_router(user_router)
app.include_router(review_router)
