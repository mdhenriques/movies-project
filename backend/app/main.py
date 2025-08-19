from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from contextlib import asynccontextmanager
from .database import test_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa ao iniciar
    test_connection()
    yield
    # Aqui você pode colocar lógica de "shutdown" se quiser
    # exemplo: fechar conexões, limpar recursos etc.

app = FastAPI(title="Movie Bank API", lifespan=lifespan)


# Exemplo de modelo
class Movie(BaseModel):
    id: int
    title: str
    year: Optional[int] = None

# Rota de teste
@app.get("/")
async def root():
    return {"message": "API do Movie Bank funcionando!"}

# Rota de teste com parâmetro
@app.get("/movie/{movie_id}")
async def get_movie(movie_id: int):
    return {"movie_id": movie_id, "title": f"Filme {movie_id}"}

# Rota de teste POST
@app.post("/movie/")
async def create_movie(movie: Movie):
    return {"message": "Filme criado com sucesso!", "movie": movie}
