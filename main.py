from fastapi import FastAPI
from db.db import engine
from db.model import Base
from fastapi.middleware.cors import CORSMiddleware
from controller.main import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PenguinHack"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return {"message": "Hello Penguin"}

app.include_router(router, prefix="/api/v1")

