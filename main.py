from fastapi import FastAPI, APIRouter
from 

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():

app.include_router(router)

