from fastapi import  Query, APIRouter
from typing import Annotated
from fastapi.responses import Response
from app.utils import find_task, write_tasks, read_tasks, filter_tasks, query_params
from app.schemas.task import TaskData, TaskUpdate, SearchFilter, TaskPutUpdate, QueryParameterSchema
# from uuid import uuid4

router = APIRouter(tags=["Tasks"])

@router.get("/",status_code=200)
def home_page():
    return {"message": "home page is ready to use."}

@router.post("/tasks", status_code=201) # 201 created
def add_tasks(data: TaskData):
    tasks = read_tasks()
    task = {"id": len(tasks)+1, **data.model_dump()}
    # task = {"id": str(uuid4()), **data.model_dump()}
    tasks.append(task)
    write_tasks(tasks)
    return task

@router.get("/tasks", status_code=200)
def list_tasks(filter: Annotated[SearchFilter, Query()], params: Annotated[QueryParameterSchema, Query()]):
    tasks = read_tasks()
    filtered_tasks = filter_tasks(filter,tasks)
    queried_tasks = query_params(params, filtered_tasks)
    return queried_tasks

@router.get("/tasks/summary", status_code=200) # yo maathi rakhnu parxa, natra task_id wala sita conflict hunxa
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
    
@router.get("/tasks/{task_id}", status_code=200)
def retrieve_task(task_id:int): # type hinting here because esle frontend bata data paauxa
    tasks = read_tasks()
    return find_task(tasks, task_id)

@router.patch("/tasks/{task_id}", status_code=200) # 200 ok
def update_task(task_id: int, data: TaskUpdate):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    task.update(data.model_dump(exclude_none=True))
    write_tasks(tasks)
    return task

@router.put("/tasks/{task_id}", status_code=200)
def put_task(task_id: int, data: TaskPutUpdate):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    task.update({"completed": False, **data.model_dump(exclude=['completed'])})
    write_tasks(tasks)
    return task

# @router.delete("/tasks/{task_id}")
@router.delete("/tasks/{task_id}", status_code=204) # 204 no content
# status code explicitly lekhe swagger docs maa response body ko laagi thaau nai naaaune raixa.
def delete_task(task_id: int):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    tasks.remove(task)
    write_tasks(tasks)
    # task["message"] = "task deleted successfully"
    # return task
    return Response(status_code=204)