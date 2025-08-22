from models import Base
from database import engine  # supondo que você tenha um engine configurado

# Cria todas as tabelas que ainda não existem
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
