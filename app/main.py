# main.py

from fastapi import FastAPI
from app.routes import AuthController  



app = FastAPI()

app.include_router(AuthController.app, prefix="/auth", tags=["auth"])

@app.head("/ping")
def read_root():
    return {"message": "Moneyline backend is live!"}

@app.get("/ping")
def read_root():
    return {"message": "Moneyline backend is live!"}

@app.get("/test")
def test_endpoint():
    return {"message": "This is a test endpoint!"}

