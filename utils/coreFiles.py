import json
import os
from pathlib import Path

RUTA_ARCHIVO = Path("data/")

def checkFile(archivo,data):
    if not (RUTA_ARCHIVO / archivo).exists():
        with open(RUTA_ARCHIVO/archivo, "w", encoding="utf-8") as cf:
            json.dump(data, cf, indent=4, ensure_ascii=False)

def readFile(archivo):
    if not (RUTA_ARCHIVO/archivo).exists():
        return {}
    with open(RUTA_ARCHIVO/archivo, "r", encoding="utf-8") as readFile:
        return json.load(readFile)

def createFile(archivo,data):
    with open(RUTA_ARCHIVO/archivo,"w+",encoding="utf-8") as createFile:
        json.dump(data, createFile, indent=4, ensure_ascii=False)