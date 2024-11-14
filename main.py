from typing import List

import uvicorn
from fastapi import FastAPI, APIRouter

from code_resources.code_resources.database import mongo_factory
from models import CodingResource

app = FastAPI()
router = APIRouter()

mongo_factory = mongo_factory()


@app.get("/resources", response_model=List[CodingResource])
async def get_resources():
    resources = list(mongo_factory.get('collection').find())
    return resources


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, reload_delay=0.5, port=8001)
