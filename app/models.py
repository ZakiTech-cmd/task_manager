from pydantic import BaseModel
from typing import Literal

class Task(BaseModel):
    id: str
    type: Literal["TYPE_A", "TYPE_B", "TYPE_C"]
    payload: str
    tokens: int

class TaskStatusUpdate(BaseModel):
    status: Literal["completed", "failed"]