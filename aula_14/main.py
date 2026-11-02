from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.db.model import criar_tabelas
from src.routes.frutas import frutas_router
from src.routes.sucos import sucos


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_tabelas()
    yield


app = FastAPI(
    title="API Para Uma Casa De Sucos",
    description="Esta é uma API que fornece informações sobre frutas e sucos de uma casa de sucos.",
    lifespan=lifespan
)

@app.get("/")
async def home():
    return {"message": "Bem-vindo à API Casa De Frutas!"}

app.include_router(frutas_router)
app.include_router(sucos)
