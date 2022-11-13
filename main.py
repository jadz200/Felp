from fastapi import Depends, FastAPI, HTTPException
from backend.endpoint.restaurant import router as restaurant_router 

app = FastAPI()


app.include_router(restaurant_router)

