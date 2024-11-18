import os
import subprocess
from typing import List, Optional

import uvicorn
from fastapi import APIRouter, Query
from fastapi import FastAPI, HTTPException

from code_resources.code_resources.database import mongo_factory
from models import CodingResource

app = FastAPI()
router = APIRouter()

mongo_factory = mongo_factory()


@app.get("/resources", response_model=List[CodingResource])
async def get_resources(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    types: Optional[List[str]] = Query(None),
    topics: Optional[List[str]] = Query(None),
    levels: Optional[List[str]] = Query(None),
    search: Optional[str] = None,
):
    skip = (page - 1) * limit
    collection = mongo_factory.get("collection")
    query = {}

    if types:
        query["types"] = {"$in": types}

    if topics:
        query["topics"] = {"$in": topics}

    if levels:
        query["levels"] = {"$in": levels}

    if search:
        query["description"] = {"$regex": search, "$options": "i"}

    resources = list(collection.find(query).skip(skip).limit(limit))

    if not resources and page != 1:
        raise HTTPException(status_code=404, detail="Page not found")

    return resources


@app.post("/fetch")
async def fetch_data():
    try:
        if os.name == "posix":
            subprocess.run(["bash", "run_scrapy.sh"], check=True)
        elif os.name == "nt":
            subprocess.run(["cmd", "/c", "run_scrapy.bat"], check=True)
        else:
            raise HTTPException(status_code=500, detail="Unsupported OS")

        return {"status": "Scraping started successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="Scraping failed to start") from e


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
