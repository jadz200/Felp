from fastapi import  FastAPI 
from backend.restaurant.endpoints import router as restaurant_router 

app = FastAPI()


app.include_router(restaurant_router)

