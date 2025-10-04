from typing import List, Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.model import ProjectModel
from app.schemas import ProjectModelCreate, ProjectModelUpdate

class DuplicateKeyException(Exception):
    pass

class MissingProjectModelException(Exception):
    pass


def get_project_model_by_key(*, db: Session, key: str) -> Optional[ProjectModel]:
    return db.query(ProjectModel).filter(ProjectModel.key == key).first()

def get_project_models(*, db: Session) -> List[ProjectModel]:
    return db.query(ProjectModel).all()

def create_project_model(*, db: Session, model: ProjectModelCreate) -> ProjectModel:
    if get_project_model_by_key(db=db, key=model.key):
        raise DuplicateKeyException()

    db_model = ProjectModel(
        key=model.key,
        title=model.title,
        explanation=model.explanation,
        project_requirements_description=model.project_requirements_description,
        project_requirements_example=model.project_requirements_example,
        team_requirements=model.team_requirements
    )

    try:
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model
    except IntegrityError as e:
        db.rollback()
        raise e


def update_project_model(
    *, db: Session, model: ProjectModelUpdate, key: str
) -> ProjectModel:
    db_model = get_project_model_by_key(db=db, key=key)

    if not db_model:
        raise MissingProjectModelException()

    # Check if new key conflicts with existing model
    if model.key and model.key != db_model.key:
        existing = get_project_model_by_key(db=db, key=model.key)
        if existing:
            raise DuplicateKeyException()

    update_data = model.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_model, key, value)

    db.commit()
    db.refresh(db_model)
    return db_model


def delete_project_model(*, db: Session, key: str) -> ProjectModel:
    db_model = get_project_model_by_key(db=db, key=key)
    
    if not db_model:
        raise MissingProjectModelException()

    db.delete(db_model)
    db.commit()

    return db_model
