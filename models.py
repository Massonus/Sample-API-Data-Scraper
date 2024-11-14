from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class CodingResource(BaseModel):
    id: int
    description: str
    url: str
    types: List[str]
    topics: List[str]
    levels: List[str]