from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from contextlib import asynccontextmanager
from .database import test_connection
from app.auth import routes as auth_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa ao iniciar
    test_connection()
    yield
    # Aqui você pode colocar lógica de "shutdown" se quiser
    # exemplo: fechar conexões, limpar recursos etc.

app = FastAPI(title="Movie Bank API", lifespan=lifespan)

app.include_router(auth_routes.router)

