# main.py

from fastapi import FastAPI

app = FastAPI()

@app.head("/ping")
def read_root():
    return {"message": "Moneyline backend is live!"}

@app.get("/ping")
def read_root():
    return {"message": "Moneyline backend is live!"}



@app.get("/test")
def test_endpoint():
    return {"message": "This is a test endpoint!"}

