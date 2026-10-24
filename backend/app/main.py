from fastapi import FastAPI
from pathlib import Path
from contextlib import asynccontextmanager

from app.routers import tasks

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
app.include_router(router=tasks.router)