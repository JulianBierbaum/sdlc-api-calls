from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/models/scrum")
def get_scrum_model():
    return {
        "title": "Scrum",
        "explanation": "Agil, mit festen Phasen (Sprints) und fixer Aufgaben pro Sprint",
        "project_requirements": {
            "description": "Agiles Projekt mit unklaren Anforderungen",
            "example": "z.B. Entwicklung einer Website für einen Kunden wo immer Feedback eingeholt wird",
        },
        "team_requirements": "Fixe Rollen, Team muss den Scrum Prozess können",
    }


@app.get("/models/iterative_incremental")
def get_iterative_incremental_model():
    return {
        "title": "Iterativer & Inkrementelles",
        "explanation": "Schrittweise Entwicklung",
        "project_requirements": {
            "description": "Projekt mit sich ändernden Anforderungen bzw. für wachsende Projekte",
            "example": "z.B. Entwicklung einer Software mit Release Cycles (Alpha, Beta, RC, Release)",
        },
        "team_requirements": "Keine besondere Schulung notwendig",
    }


@app.get("/models/kanban")
def get_kanban_model():
    return {
        "title": "Kanban",
        "explanation": "Agil, Visualisierung auf Kanban-Board, Tasks können im Board vor und zurück gehen",
        "project_requirements": {
            "description": "Agile Projekte mit sich ändernder Priorität",
            "example": "z.B. Wartung von Systemen wo immer Aufgaben mit unterschiedlichen Prioritäten anliegen",
        },
        "team_requirements": "Team muss sich gut selbst organisieren können",
    }


@app.get("/models/spiral")
def get_spiral_model():
    return {
        "title": "spiral",
        "explanation": "Neues Ziel pro Durchlauf, Phasen werden pro Durchlauf durchgemacht",
        "project_requirements": {
            "description": "Große, Komplexe Modelle",
            "example": "z.B. Entwicklung einer großen Software wo das Projekt in einzelne Komponenten oder Phasen aufgeteilt werden muss",
        },
        "team_requirements": "Keine besonderen Anforderungen",
    }


@app.get("/models/v")
def get_v_model():
    return {
        "title": "V-Modell",
        "explanation": "Klassisch Sequenziell mit genauem Testen bei jeder Phase",
        "project_requirements": {
            "description": "Kritische Projekte",
            "example": "z.B. Entwicklung eines Kritischen Systems (Ampelsystem)",
        },
        "team_requirements": "Keine besonderen Anforderungen",
    }


@app.get("/models/waterfall")
def get_waterfall_model():
    return {
        "title": "Wasserfallmodell",
        "explanation": "Klassisch, fester Ablauf der Phase",
        "project_requirements": {
            "description": "Genaue Anforderungen für einen bekannten Projekttyp",
            "example": "z.B. Entwicklung einer Website für eine Regierung, welche fixen Anforderungen entsprechen soll",
        },
        "team_requirements": "Keine besonderen Anforderungen",
    }


@app.post("/models/xp")
def post_xp_model(title: str):
    if title == "xp":
        return {"title": "Extreme Programming"}
    else:
        return HTTPException(status_code=404, detail="title not found")

@app.post("/models/rup")
def post_rup_model(title: str):
    if title == "rup":
        return {"title": "Rational Unified Process"}
    else:
        return HTTPException(status_code=404, detail="title not found")
