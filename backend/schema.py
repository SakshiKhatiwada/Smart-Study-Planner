from pydantic import BaseModel, EmailStr

class TaskData(BaseModel):
    fullName: str
    email: EmailStr
    phone: str | None = None
    
class TaskUpdate(BaseModel): # update maa optional hunxan, so we create separately
    fullName: str | None = None
    email: EmailStr | None = None
    phone: str | None = None