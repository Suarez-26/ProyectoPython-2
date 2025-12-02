import json
import os

RUTA_JSON = "data/gastos.json"

def cargar_datos():
    if not os.path.exists(RUTA_JSON):
        return []

    with open(RUTA_JSON, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def guardar_datos(data):
    with open(RUTA_JSON, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
