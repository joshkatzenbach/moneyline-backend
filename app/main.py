# main.py

from fastapi import FastAPI
from app.routes import AuthController  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow ALL origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows any origin
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(AuthController.app, prefix="/auth", tags=["auth"])

@app.head("/ping")
def read_root():
    return {"message": "Moneyline backend is live!"}

@app.get("/test")
def test_endpoint():
    return {"message": "This is in prod"}

