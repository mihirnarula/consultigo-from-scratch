from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps
from app.schemas.guesstimate import Guesstimate, GuesstimateCreate, GuesstimateUpdate

router = APIRouter()


@router.get("/", response_model=List[Guesstimate])
def read_guesstimate(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve guesstimate entries.
    """
    # If current user is superuser, get all guesstimate entries
    if current_user.is_superuser:
        guesstimate = crud.guesstimate.get_multi(db, skip=skip, limit=limit)
    else:
        # Otherwise get only user's own guesstimate entries
        guesstimate = crud.guesstimate.get_multi_by_user(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    return guesstimate


@router.post("/", response_model=Guesstimate)
def create_guesstimate(
    *,
    db: Session = Depends(deps.get_db),
    guesstimate_in: GuesstimateCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new guesstimate entry.
    """
    guesstimate = crud.guesstimate.create_with_user(
        db=db, obj_in=guesstimate_in, user_id=current_user.id
    )
    return guesstimate


@router.put("/{id}", response_model=Guesstimate)
def update_guesstimate(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    guesstimate_in: GuesstimateUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update a guesstimate entry.
    """
    guesstimate = crud.guesstimate.get(db=db, id=id)
    if not guesstimate:
        raise HTTPException(status_code=404, detail="Guesstimate not found")
    if guesstimate.user_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    guesstimate = crud.guesstimate.update(db=db, db_obj=guesstimate, obj_in=guesstimate_in)
    return guesstimate


@router.get("/{id}", response_model=Guesstimate)
def read_guesstimate_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get a specific guesstimate entry by id.
    """
    guesstimate = crud.guesstimate.get(db=db, id=id)
    if not guesstimate:
        raise HTTPException(status_code=404, detail="Guesstimate not found")
    if guesstimate.user_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return guesstimate


@router.delete("/{id}", response_model=Guesstimate)
def delete_guesstimate(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Delete a guesstimate entry.
    """
    guesstimate = crud.guesstimate.get(db=db, id=id)
    if not guesstimate:
        raise HTTPException(status_code=404, detail="Guesstimate not found")
    if guesstimate.user_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    guesstimate = crud.guesstimate.remove(db=db, id=id)
    return guesstimate 