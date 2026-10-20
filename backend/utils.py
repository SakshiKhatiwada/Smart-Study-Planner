from fastapi import HTTPException
import json
from uuid import uuid4
from pathlib import Path

tasks_FILE = Path(__file__).with_name("tasks.json")

def find_task(tasks, task_id):
    # Search- Linear
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="task Not Found") # 404 not found

def write_tasks(tasks):
    with open(tasks_FILE, "w", encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)
        
def read_tasks():
    try:
        with open(tasks_FILE, "r", encoding='utf-8') as file:
            tasks = json.load(file)
        if not isinstance(tasks, list):
            raise ValueError("Expected a list")
        return tasks
    
    except FileNotFoundError:
        return []
    
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid task JSON file") # 500 Internal Server Error