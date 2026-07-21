from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    # Busca a tarefa no banco
    task = db.query(Task).filter(Task.id == task_id).first()

    # Se não existir, retorna erro
    if not task:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # Atualiza apenas os campos enviados
    update_data = task_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    # Salva as alterações
    db.commit()

    # Atualiza o objeto
    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # Busca a tarefa
    task = db.query(Task).filter(Task.id == task_id).first()

    # Verifica se existe
    if not task:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # Remove do banco
    db.delete(task)

    # Confirma a remoção
    db.commit()

    return {"message": f"Tarefa {task_id} removida com sucesso"}
