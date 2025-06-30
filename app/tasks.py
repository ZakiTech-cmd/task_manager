import random
import string
import uuid
from models import Task

def generate_random_task() -> Task:
    task_type = random.choice(["TYPE_A", "TYPE_B", "TYPE_C"])
    payload_length = random.randint(100, 200)
    payload = ''.join(random.choices(string.ascii_letters + string.digits + " ", k=payload_length))
    tokens = random.randint(10, 50)
    return Task(
        id=str(uuid.uuid4()),
        type=task_type,
        payload=payload,
        tokens=tokens
    )
