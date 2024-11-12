from datetime import datetime
from pydantic import BaseModel, Field

class Todo(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    is_deleted: bool = False
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    creation: datetime = Field(default_factory=datetime.utcnow)
