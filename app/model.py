from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectModel(Base):
    __tablename__ = "project_models"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    explanation = Column(Text)
    project_requirements_description = Column(Text)
    project_requirements_example = Column(Text)
    team_requirements = Column(Text)
