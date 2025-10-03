from fastapi import FastAPI, HTTPException

from crud import get_model

app = FastAPI()


@app.get("/models/scrum")
def get_scrum_model():
    return get_model(model_name="scrum")


@app.get("/models/iterative_incremental")
def get_iterative_incremental_model():
    return get_model(model_name="iterative_incremental")


@app.get("/models/kanban")
def get_kanban_model():
    return get_model(model_name="kanban")


@app.get("/models/spiral")
def get_spiral_model():
    return get_model(model_name="spiral")


@app.get("/models/v")
def get_v_model():
    return get_model(model_name="v")


@app.get("/models/waterfall")
def get_waterfall_model():
    return get_model(model_name="waterfall")


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
