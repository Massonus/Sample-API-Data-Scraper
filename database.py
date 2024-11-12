import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_DETAILS)
database = client.todo_db
collection = database["items"]


async def check_db_connection():
    try:
        await client.admin.command("ping")
        print("Successfully connected to MongoDB!")
    except ServerSelectionTimeoutError:
        print("Could not connect to MongoDB. Please check your connection.")
