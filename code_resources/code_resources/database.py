import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")


def mongo_factory():
    client = MongoClient(MONGO_DETAILS)
    database = client.code_resources
    collection = database["resources"]
    return {'client': client, 'db': database, 'collection': collection}
