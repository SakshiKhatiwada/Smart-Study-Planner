from fastapi import FastAPI, Query
from typing import Annotated
from fastapi.responses import Response
from utils import find_task, write_tasks, read_tasks
from schema import TaskData, TaskUpdate, SearchFilter
# from uuid import uuid4
from pathlib import Path
from contextlib import asynccontextmanager
import json

TASKS_FILE = Path(__file__).with_name("tasks.json")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs when the API starts
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "w") as file:
            json.dump([], file) 
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/",status_code=200)
def home_page():
    return {"message": "home page is ready to use."}

@app.post("/tasks", status_code=201) # 201 created
def add_tasks(data: TaskData):
    tasks = read_tasks()
    task = {"id": len(tasks)+1, **data.model_dump()}
    # task = {"id": str(uuid4()), **data.model_dump()}
    tasks.append(task)
    write_tasks(tasks)
    return task

@app.get("/tasks", status_code=200)
def list_tasks(filter: Annotated[SearchFilter, Query()]):
    results = read_tasks()
    if filter.search_subject is not None:
        results = [
            task for task in results
            if filter.search_subject.lower() in task["subject"].lower()
        ]
        
    if filter.completed_status is not None:
        results = [
            task for task in results 
            if filter.completed_status == task['completed']
        ]
        
    if filter.search is not None:
        results = [
            task for task in results 
            if filter.search.lower() in task["title"]
        ]
        
    return results

    # if filter.search_title is not None:
    #     results = [
    #         task for task in results 
    #         if filter.search_title.lower() == task['title'].lower()
    #     ]
        
    # if filter.search_priority is not None:
    #     results = [
    #         task for task in results 
    #         if filter.search_priority == task['priority']
    #     ]
    # return results

@app.get("/tasks/{task_id}", status_code=200)
def retrieve_task(task_id:int): # type hinting here because esle frontend bata data paauxa
    tasks = read_tasks()
    return find_task(tasks, task_id)

@app.patch("/tasks/{task_id}", status_code=200) # 200 ok
def update_task(task_id: int, data: TaskUpdate):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    task.update(data.model_dump(exclude_none=True))
    write_tasks(tasks)
    return task

# @app.delete("/tasks/{task_id}")
@app.delete("/tasks/{task_id}", status_code=204) # 204 no content
# status code explicitly lekhe swagger docs maa response body ko laagi thaau nai naaaune raixa.
def delete_task(task_id):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    tasks.remove(task)
    write_tasks(tasks)
    # task["message"] = "task deleted successfully"
    # return task
    return Response(status_code=204)