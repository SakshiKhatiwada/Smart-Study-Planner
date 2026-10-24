from pydantic import BaseModel, Field
from typing import Literal
from fastapi import Query
from typing import Annotated
# from uuid import uuid4

class TaskData(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    subject: Annotated[str, Field(min_length=2)]
    priority: Literal["low", "medium", "high"] = "low"
    completed: bool = False
    estimated_minutes: Annotated[int, Field(ge=1, le=480)]
    
class TaskUpdate(BaseModel): # update maa optional hunxan, so we create separately
    title: Annotated[str | None, Field(min_length=3)] = None
    subject: Annotated[str | None, Field(min_length=2)] = None
    priority: Literal["low", "medium", "high"] = "low"
    completed: bool = False
    estimated_minutes: Annotated[int | None, Field(ge=1, le=480)] = None
      
class TaskPutUpdate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    subject: Annotated[str, Field(min_length=2)]
    priority: Literal["low", "medium", "high"]
    estimated_minutes: Annotated[int, Field(ge=1, le=480)]
    
class SearchFilter(BaseModel):
    search_subject: str | None = None
    completed_status: bool | None = None
    search: str | None = None
    # search_priority: str | None = None
    # search_priority: str | None = None
    
class QueryParameterSchema(BaseModel):
    priority: Literal["low", "medium", "high"] | None= None
    skip: Annotated[int | None, Field(ge=0)] = 0
    limit: Annotated[int | None, Field(ge=1, le=20)] = 10
    sort_by: Literal["title", "estimated_minutes"] = "title"
    order: Literal["asc", "desc"] = "asc"