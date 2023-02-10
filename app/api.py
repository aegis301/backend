from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.data import router as DataRouter
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

app.include_router(DataRouter, tags=["Data"], prefix="/data")

origins = ["http://localhost:3000", "localhost:3000", "https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
