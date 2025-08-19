from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/moviedb"
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexão bem-sucedida! Resultado:", result.scalar())
    except SQLAlchemyError as e:
        print("Erro ao conectar no banco:", e)