from fastapi import FastAPI, Query
from typing import Annotated
from fastapi.responses import Response
from utils import find_task, write_tasks, read_tasks, filter_tasks, query_params
from schema import TaskData, TaskUpdate, SearchFilter, TaskPutUpdate, QueryParameterSchema
# from uuid import uuid4
from pathlib import Path
from contextlib import asynccontextmanager
import json

TASKS_FILE = Path(__file__).with_name("tasks.json")

# @asynccontextmanager # if we want to clear the file data at every startup
# async def lifespan(app: FastAPI):
#     # Runs when the API starts
#     if TASKS_FILE.exists():
#         with open(TASKS_FILE, "w") as file:
#             json.dump([], file) 
#     yield
    
# app = FastAPI(lifespan=lifespan)
app = FastAPI()

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
def list_tasks(filter: Annotated[SearchFilter, Query()], params: Annotated[QueryParameterSchema, Query()]):
    tasks = read_tasks()
    filtered_tasks = filter_tasks(filter,tasks)
    queried_tasks = query_params(params, filtered_tasks)
    return queried_tasks

@app.get("/tasks/summary", status_code=200) # yo maathi rakhnu parxa, natra task_id wala sita conflict hunxa
# Route tip: declare /tasks/summary before /tasks/{task_id}, so FastAPI does not interpret the word “summary” as an ID.
def get_summary():
    tasks = read_tasks()
    summary = {}
    
    summary["total_tasks"] = int(len(tasks))
    # summary["completed_tasks"] =  len(
    #     [task for task in tasks
    #      if task["completed_tasks"] == True]
    # )
    
    summary["completed_tasks"] = int(sum(task['completed'] for task in tasks))
    
    summary["pending_tasks"] = summary["total_tasks"] - summary["completed_tasks"] 
    
    summary["total_estimated_minutes"] = sum(task['estimated_minutes'] for task in tasks)
    
    summary["remaining_estimated_minutes"] = sum(task["estimated_minutes"] for task in tasks if task['completed'] == False)
    
    return summary
    
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

@app.put("/tasks/{task_id}", status_code=200)
def put_task(task_id: int, data: TaskPutUpdate):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    task.update({"completed": False, **data.model_dump(exclude=['completed'])})
    write_tasks(tasks)
    return task

# @app.delete("/tasks/{task_id}")
@app.delete("/tasks/{task_id}", status_code=204) # 204 no content
# status code explicitly lekhe swagger docs maa response body ko laagi thaau nai naaaune raixa.
def delete_task(task_id: int):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    tasks.remove(task)
    write_tasks(tasks)
    # task["message"] = "task deleted successfully"
    # return task
    return Response(status_code=204)