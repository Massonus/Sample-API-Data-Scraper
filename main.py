from datetime import datetime

import uvicorn
from bson import ObjectId
from fastapi import FastAPI, APIRouter, HTTPException

from database import collection
from models import Todo
from shcemas import todos_data

app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_todos():
    data = collection.find()
    return todos_data(data)


@router.post("/")
async def add_todo(todo: Todo):
    try:
        response = collection.insert_one(dict(todo))
        return {"stasus_code": 201, "id": str(response.inserted_id)}
    except Exception:
        return HTTPException(status_code=500, detail="Something went wrong")


@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Task does not exist")

        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id": id}, {"$set": dict(updated_task)})
        return {"status_code": 200, "message": "Task Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occurred {e}")


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")

        resp = collection.delete_one({"_id": id})

        if resp.deleted_count == 0:
            raise HTTPException(status_code=500, detail="Failed to delete the task")

        return {"status_code": 200, "message": "Task Deleted Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, reload_delay=0.5, port=8001)
