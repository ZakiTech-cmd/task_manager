from fastapi import APIRouter, HTTPException, Request, Depends
from starlette import status
from fastapi import Response

from models import Task, TaskStatusUpdate
from storage import task_queue, in_progress_tasks

router = APIRouter()

API_KEY = "my-secret-token"

def check_auth(request: Request):
    if request.headers.get("X-API-KEY") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
@router.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

@router.get("/tasks")
def get_all_tasks():
    return task_queue

@router.post("/new_task")
def create_task(task: Task, _: None = Depends(check_auth)):
    task_queue.append(task)
    return {"message": "Task created", "task_id": task.id}

@router.get("/next_task")
def get_next_task(_: None = Depends(check_auth)):
    if not task_queue:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    next_task = task_queue.pop(0)
    in_progress_tasks[next_task.id] = next_task
    return next_task

@router.post("/update_task/{task_id}")
def update_task_status(task_id: str, update: TaskStatusUpdate, _: None = Depends(check_auth)):
    task = in_progress_tasks.pop(task_id, None)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID not found or already updated")

    if update.status == "failed":
        task_queue.append(task)  # Requeue

    return {"message": f"Task {task_id} marked as {update.status}"}
