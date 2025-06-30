import requests
import time
import random

API_URL = "http://127.0.0.1:8000"
HEADERS = {"X-API-KEY": "my-secret-token"}

token_bank = random.randint(200, 1000)
print(f"Agent started with {token_bank} tokens")

while True:
    try:
        response = requests.get(f"{API_URL}/next_task", headers=HEADERS)
        if response.status_code == 204:
            print("No task available. Waiting 30s...")
            time.sleep(30)
            continue

        task = response.json()
        task_id = task["id"]
        tokens_needed = task["tokens"]
        print(f"Got task {task_id} (needs {tokens_needed} tokens)")

        if token_bank >= tokens_needed:
            work_time = random.randint(3, 5)
            print(f"Working {work_time}s...")
            time.sleep(work_time)
            token_bank -= tokens_needed
            status = "completed"
            print(f"Task {task_id} completed! Remaining tokens: {token_bank}")
        else:
            status = "failed"
            print(f"Not enough tokens for task {task_id}. Marking as failed.")

        requests.post(
            f"{API_URL}/update_task/{task_id}",
            headers={**HEADERS, "Content-Type": "application/json"},
            json={"status": status},
        )

    except Exception as e:
        print(f"Error occurred: {e}")

    time.sleep(1)
