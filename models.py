from typing import List

from pydantic import BaseModel


class CodingResource(BaseModel):
    id: int
    description: str
    url: str
    types: List[str]
    topics: List[str]
    levels: List[str]
