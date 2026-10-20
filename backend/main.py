from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from utils import find_task, write_tasks, read_tasks
from schema import TaskData, TaskUpdate
from uuid import uuid4

app = FastAPI()

@app.get("/",status_code=200)
def home_page():
    return {"message": "home page is ready to use."}

@app.post("/tasks", status_code=201) # 201 created
def add_tasks(data: TaskData):
    tasks = read_tasks()
    task = {"id": str(uuid4()), **data.model_dump()}
    tasks.append(task)
    write_tasks(tasks)
    return task

@app.get("/tasks", status_code=200)
def list_tasks():
    tasks = read_tasks()
    return tasks

@app.get("/tasks/{task_id}", status_code=200)
def retrieve_task(task_id:str): # type hinting here because esle frontend bata data paauxa
    tasks = read_tasks()
    return find_task(tasks, task_id)

@app.patch("/tasks/{task_id}", status_code=200) # 200 ok
def update_task(task_id: str, data: TaskUpdate):
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
    task["message"] = "task deleted successfully"
    # return task
    return Response(status_code=204)