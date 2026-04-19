from fastapi import FastAPI
from rag import preguntar

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.get("/preguntar")
def query(pregunta: str):
    respuesta = preguntar(pregunta)
    return {"respuesta": respuesta}