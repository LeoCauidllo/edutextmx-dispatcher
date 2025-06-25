from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import datetime

app = FastAPI(title="EduTextMx Dispatcher", version="0.1")

usb_nodes = {
    "usb_001": {"status": "online", "last_seen": str(datetime.datetime.now())},
    "usb_002": {"status": "offline", "last_seen": None}
}

class TaskRequest(BaseModel):
    url: str
    priority: Optional[int] = 1

class NodeStatus(BaseModel):
    node_id: str
    status: str
    last_seen: Optional[str]

class OCRResult(BaseModel):
    raw_text: str
    confidence: float
    source_node: str
    analysis_needed: bool

@app.get("/health")
def health_check():
    return {"status": "Dispatcher is running", "timestamp": str(datetime.datetime.now())}

@app.post("/receive_task")
def receive_task(task: TaskRequest):
    return {"message": "Task received", "url": task.url, "priority": task.priority}

@app.get("/node_status", response_model=List[NodeStatus])
def get_node_status():
    return [
        {"node_id": node, "status": data["status"], "last_seen": data["last_seen"]}
        for node, data in usb_nodes.items()
    ]

@app.post("/results")
def receive_result(result: OCRResult):
    return {"message": "Result received", "source": result.source_node}
