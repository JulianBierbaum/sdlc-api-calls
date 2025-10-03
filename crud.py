import json

with open("models.json", encoding="utf-8") as f:
    data = json.load(f)


def get_model(model_name: str):
    model_name = model_name.lower()
    
    if model_name in data["models"]:
        return data["models"][model_name]
    return None
