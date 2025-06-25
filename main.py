from fastapi import FastAPI, Request
from typing import Dict, List
from datetime import datetime

app = FastAPI()

# Simulación de nodos activos
usb_nodes = {
    "usb_001": {"status": "online", "last_seen": datetime.utcnow()},
    "usb_002": {"status": "offline", "last_seen": None},
}

@app.get("/health")
def get_health():
    return {"status": "Dispatcher running"}

@app.post("/receive_task")
async def receive_task(request: Request):
    data = await request.json()
    url = data.get("url")
    return {"message": "Tarea recibida", "url": url}

@app.get("/node_status")
def node_status():
    return usb_nodes

@app.post("/results")
async def receive_results(request: Request):
    data = await request.json()
    return {"message": "Resultado recibido", "data": data}
