from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Todo])
def read_todos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve todos.
    """
    todos = crud.todo.get_multi_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return todos

@router.post("/", response_model=schemas.Todo)
def create_todo(
    *,
    db: Session = Depends(deps.get_db),
    todo_in: schemas.TodoCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new todo.
    """
    todo = crud.todo.create_with_user(db=db, obj_in=todo_in, user_id=current_user.id)
    return todo

@router.put("/{todo_id}", response_model=schemas.Todo)
def update_todo(
    *,
    db: Session = Depends(deps.get_db),
    todo_id: int,
    todo_in: schemas.TodoUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a todo.
    """
    todo = crud.todo.get_by_user(db=db, user_id=current_user.id, todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = crud.todo.update(db=db, db_obj=todo, obj_in=todo_in)
    return todo

@router.delete("/{todo_id}", response_model=schemas.Todo)
def delete_todo(
    *,
    db: Session = Depends(deps.get_db),
    todo_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a todo.
    """
    todo = crud.todo.get_by_user(db=db, user_id=current_user.id, todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = crud.todo.remove(db=db, id=todo_id)
    return todo 