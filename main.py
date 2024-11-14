from typing import List

import uvicorn
from fastapi import FastAPI, APIRouter, Query, HTTPException

from code_resources.code_resources.database import mongo_factory
from models import CodingResource

app = FastAPI()
router = APIRouter()

mongo_factory = mongo_factory()


@app.get("/resources", response_model=List[CodingResource])
async def get_resources(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    skip = (page - 1) * limit
    resources = list(mongo_factory.get('collection').find().skip(skip).limit(limit))

    if not resources and page != 1:
        raise HTTPException(status_code=404, detail="Page not found")

    return resources


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, reload_delay=0.5, port=8001)
