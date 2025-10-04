from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model import Base, ProjectModel

DATABASE_URL = "postgresql://admin:Kennwort1@localhost:5432/app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency for getting database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

INITIAL_DATA = {
    "scrum": {
        "title": "Scrum",
        "explanation": "Agil, mit festen Phasen (Sprints) und fixer Aufgaben pro Sprint",
        "project_requirements": {
            "description": "Agiles Projekt mit unklaren Anforderungen",
            "example": "z.B. Entwicklung einer Website für einen Kunden wo immer Feedback eingeholt wird"
        },
        "team_requirements": "Fixe Rollen, Team muss den Scrum Prozess können"
    },
    "iterative_incremental": {
        "title": "Iterativer & Inkrementelles",
        "explanation": "Schrittweise Entwicklung",
        "project_requirements": {
            "description": "Projekt mit sich ändernden Anforderungen bzw. für wachsende Projekte",
            "example": "z.B. Entwicklung einer Software mit Release Cycles (Alpha, Beta, RC, Release)"
        },
        "team_requirements": "Keine besondere Schulung notwendig"
    },
    "kanban": {
        "title": "Kanban",
        "explanation": "Agil, Visualisierung auf Kanban-Board, Tasks können im Board vor und zurück gehen",
        "project_requirements": {
            "description": "Agile Projekte mit sich ändernder Priorität",
            "example": "z.B. Wartung von Systemen wo immer Aufgaben mit unterschiedlichen Prioritäten anliegen"
        },
        "team_requirements": "Team muss sich gut selbst organisieren können"
    },
    "spiral": {
        "title": "spiral",
        "explanation": "Neues Ziel pro Durchlauf, Phasen werden pro Durchlauf durchgemacht",
        "project_requirements": {
            "description": "Große, Komplexe Modelle",
            "example": "z.B. Entwicklung einer großen Software wo das Projekt in einzelne Komponenten oder Phasen aufgeteilt werden muss"
        },
        "team_requirements": "Keine besonderen Anforderungen"
    },
    "v": {
        "title": "V-Modell",
        "explanation": "Klassisch Sequenziell mit genauem Testen bei jeder Phase",
        "project_requirements": {
            "description": "Kritische Projekte",
            "example": "z.B. Entwicklung eines Kritischen Systems (Ampelsystem)"
        },
        "team_requirements": "Keine besonderen Anforderungen"
    },
    "waterfall": {
        "title": "Wasserfallmodell",
        "explanation": "Klassisch, fester Ablauf der Phase",
        "project_requirements": {
            "description": "Genaue Anforderungen für einen bekannten Projekttyp",
            "example": "z.B. Entwicklung einer Website für eine Regierung, welche fixen Anforderungen entsprechen soll"
        },
        "team_requirements": "Keine besonderen Anforderungen"
    },
    "xp": {
        "title": "Extreme Programming"
    },
    "rup": {
        "title": "Rational Unified Process"
    }
}


def init_db():
    """Initialize database and populate with initial data if empty."""
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        existing_count = db.query(ProjectModel).count()
        if existing_count > 0:
            print("Database already initialized")
            return
        
        for key, data in INITIAL_DATA.items():
            model = ProjectModel(
                key=key,
                title=data.get("title"),
                explanation=data.get("explanation"),
                project_requirements_description=data.get("project_requirements", {}).get("description"),
                project_requirements_example=data.get("project_requirements", {}).get("example"),
                team_requirements=data.get("team_requirements")
            )
            db.add(model)
        
        db.commit()
        print(f"Database initialized with {len(INITIAL_DATA)} project models")
    finally:
        db.close()
