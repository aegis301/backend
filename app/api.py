import os

from .db import SQLALCHEMY_DATABASE_URL
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from .routes.vitalsign import router as VitalsignRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db


app = FastAPI()

app.include_router(VitalsignRouter, tags=["Data"], prefix="/data")

origins = ["http://localhost:3000", "localhost:3000", "https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
