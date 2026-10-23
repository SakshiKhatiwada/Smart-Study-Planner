from pydantic import BaseModel, Field
from typing import Literal
# from fastapi import Query
from typing import Annotated
# from uuid import uuid4

class TaskData(BaseModel):
    # id: str
    title: Annotated[str, Field(min_length=3)]
    subject: Annotated[str, Field(min_length=2)]
    priority: Literal["low", "medium", "high"] = "low"
    completed: bool = False
    estimated_minutes: Annotated[int, Field(ge=1, le=480)]
    
class TaskUpdate(BaseModel): # update maa optional hunxan, so we create separately
    # id: str | None = None
    title: Annotated[str | None, Field(min_length=3)] = None
    subject: Annotated[str | None, Field(min_length=2)] = None
    priority: Literal["low", "medium", "high"] = "low"
    completed: bool = False
    estimated_minutes: Annotated[int | None, Field(ge=1, le=480)] = None