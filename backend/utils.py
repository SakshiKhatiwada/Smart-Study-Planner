from fastapi import HTTPException
from schema import SearchFilter, QueryParameterSchema
import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")

def find_task(tasks, task_id):
    # Search- Linear
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="task Not Found") # 404 not found

def write_tasks(tasks):
    with open(TASKS_FILE, "w", encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)
        
def read_tasks():
    try:
        with open(TASKS_FILE, "r", encoding='utf-8') as file:
            tasks = json.load(file)
        if not isinstance(tasks, list):
            raise ValueError("Expected a list")
        return tasks
    
    except FileNotFoundError:
        return []
    
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid task JSON file") # 500 Internal Server Error
    
# def reset_tasks():
#     with open(TASKS_FILE, "w", encoding='utf-8') as file:
#         # file.truncate(0)
#         pass

def filter_tasks(filter: SearchFilter, results):
    
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

def query_params(params, results):
    if params.priority is not None:
       results = [
            task for task in results
            if task["priority"]  == params.priority
        ]
        
    if params.sort_by:
       results= sorted(
           results, 
           key=lambda task:  task[params.sort_by],
           reverse= (params.order == "desc")
           )
       
    if params.limit is not None and params.skip is not None:
        results = results[params.skip:params.skip + params.limit]
        
    return results