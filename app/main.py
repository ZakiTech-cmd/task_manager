from fastapi import FastAPI
from routes import router
from storage import task_queue
from tasks import generate_random_task

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def initialize_tasks():
    for _ in range(20):
        task_queue.append(generate_random_task())
    print("Initialized with 20 random tasks.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)