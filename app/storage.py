from typing import List, Dict
from models import Task

task_queue: List[Task] = []
in_progress_tasks: Dict[str, Task] = {}
