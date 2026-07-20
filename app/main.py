from fastapi import FastAPI
from app.database import engine, Base
from app import models

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task API",
    description="API de gerenciamento de tarefas",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "API funcionando"}