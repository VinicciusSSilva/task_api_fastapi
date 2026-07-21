from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes.tasks import router as tasks_router

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task API",
    description="API de gerenciamento de tarefas",
    version="1.0.0"
)

app.include_router(tasks_router)
                   
@app.get("/")
def home():
    return {"message": "API funcionando"}