from pydantic import BaseModel, Field
from typing import Optional


class ProjectModelBase(BaseModel):
    key: str = Field(..., min_length=1, max_length=100)
    title: str = Field(..., min_length=1, max_length=200)
    explanation: Optional[str] = Field(None)
    project_requirements_description: Optional[str] = Field(None)
    project_requirements_example: Optional[str] = Field(None)
    team_requirements: Optional[str] = Field(None)


class ProjectModelCreate(ProjectModelBase):
    pass


class ProjectModelUpdate(BaseModel):
    key: Optional[str] = Field(None, min_length=1, max_length=100)
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    explanation: Optional[str] = None
    project_requirements_description: Optional[str] = None
    project_requirements_example: Optional[str] = None
    team_requirements: Optional[str] = None


class ProjectModelInDB(ProjectModelBase):
    id: int

    class Config:
        from_attributes = True


class ProjectModel(ProjectModelInDB):
    pass
