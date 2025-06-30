import requests
import random
import string
import time
import uuid

print("Starting Task Creator...")
API_URL = "http://127.0.0.1:8000/new_task"
HEADERS = {"X-API-KEY": "my-secret-token", "Content-Type": "application/json"}

def generate_random_payload():
    length = random.randint(100, 200)
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

while True:
    try:
        task = {
            "id": str(uuid.uuid4()),
            "type": random.choice(["TYPE_A", "TYPE_B", "TYPE_C"]),
            "payload": generate_random_payload(),
            "tokens": random.randint(10, 50),
        }

        response = requests.post(API_URL, headers=HEADERS, json=task)

        if response.status_code == 200:
            print(f"Task {task['id']} created.")
        else:
            print(f"Failed to create task: {response.status_code} {response.text}")

        sleep_time = random.randint(30, 60)
        print(f"Waiting {sleep_time}s before creating next task...")
        time.sleep(sleep_time)

    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(10)
