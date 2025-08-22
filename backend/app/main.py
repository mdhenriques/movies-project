from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from contextlib import asynccontextmanager
from .database import test_connection
from app.auth import routes as auth_routes
from app.routes import import_movies as import_routes
from app.routes import search as search_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    test_connection()
    yield

app = FastAPI(title="Movie Bank API", lifespan=lifespan)

app.include_router(auth_routes.router)
app.include_router(import_routes.router)
app.include_router(search_routes.router)


