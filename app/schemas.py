from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Dados que o usuário envia para criar uma tarefa
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "media"

# Dados que a API devolve para o cliente
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True

#Faz o update no banco de dados
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    completed: Optional[bool] = None

        