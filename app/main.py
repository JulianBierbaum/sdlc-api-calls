from typing import List
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.db import init_db, get_db
import app.crud as crud
from app.schemas import ProjectModel, ProjectModelCreate, ProjectModelUpdate

app = FastAPI()

init_db()


@app.get("/models", response_model=List[ProjectModel])
def list_models(db: Session = Depends(get_db)):
    return crud.get_project_models(db=db)


@app.get("/models/{key}", response_model=ProjectModel)
def get_model(key: str, db: Session = Depends(get_db)):
    model = crud.get_project_model_by_key(db=db, key=key)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project model with key '{key}' not found"
        )
    return model


@app.post("/models", response_model=ProjectModel, status_code=status.HTTP_201_CREATED)
def create_model(
    model: ProjectModelCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_project_model(db=db, model=model)
    except crud.DuplicateKeyException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Project model with key '{model.key}' already exists"
        )


@app.put("/models/{key}", response_model=ProjectModel)
def update_model(
    key: str,
    model: ProjectModelUpdate,
    db: Session = Depends(get_db)
):
    try:
        return crud.update_project_model(db=db, model=model, key=key)
    except crud.MissingProjectModelException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project model with key '{key}' not found"
        )
    except crud.DuplicateKeyException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Project model with key '{model.key}' already exists"
        )


@app.patch("/models/{key}", response_model=ProjectModel)
def partial_update_model(
    key: str,
    model: ProjectModelUpdate,
    db: Session = Depends(get_db)
):
    try:
        return crud.update_project_model(db=db, model=model, key=key)
    except crud.MissingProjectModelException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project model with key '{key}' not found"
        )
    except crud.DuplicateKeyException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Project model with key '{model.key}' already exists"
        )


@app.delete("/models/{key}", response_model=ProjectModel)
def delete_model(key: str, db: Session = Depends(get_db)):
    try:
        return crud.delete_project_model(db=db, key=key)
    except crud.MissingProjectModelException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project model with key '{key}' not found"
        )


@app.get("/models/scrum", response_model=ProjectModel)
def get_scrum_model(db: Session = Depends(get_db)):
    return get_model(key="scrum", db=db)


@app.get("/models/iterative_incremental", response_model=ProjectModel)
def get_iterative_incremental_model(db: Session = Depends(get_db)):
    return get_model(key="iterative_incremental", db=db)


@app.get("/models/kanban", response_model=ProjectModel)
def get_kanban_model(db: Session = Depends(get_db)):
    return get_model(key="kanban", db=db)


@app.get("/models/spiral", response_model=ProjectModel)
def get_spiral_model(db: Session = Depends(get_db)):
    return get_model(key="spiral", db=db)


@app.get("/models/v", response_model=ProjectModel)
def get_v_model(db: Session = Depends(get_db)):
    return get_model(key="v", db=db)


@app.get("/models/waterfall", response_model=ProjectModel)
def get_waterfall_model(db: Session = Depends(get_db)):
    return get_model(key="waterfall", db=db)


@app.get("/models/xp", response_model=ProjectModel)
def get_xp_model(db: Session = Depends(get_db)):
    return get_model(key="xp", db=db)


@app.get("/models/rup", response_model=ProjectModel)
def get_rup_model(db: Session = Depends(get_db)):
    return get_model(key="rup", db=db)
