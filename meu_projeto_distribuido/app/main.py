# app/main.py
from fastapi import FastAPI
import socket

app = FastAPI()

# Pega o hostname do container para sabermos qual instância respondeu
hostname = socket.gethostname()

@app.get("/")
def read_root():
    return {
        "message": "Olá, mundo! Esta resposta veio do container:",
        "hostname": hostname
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {
        "item_id": item_id,
        "q": q,
        "message": f"Resposta do container {hostname}"
    }