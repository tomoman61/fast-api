from typing import Optional

from pydantic import BaseModel, Field

# Base
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

# Create Model
class TaskCreate(TaskBase):
    pass

# Create Response
class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True

# Read
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        from_attributes = True