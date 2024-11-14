from .database import mongo_factory

mongo_factory = mongo_factory()


class MongoPipeline:
    def __init__(self):
        self.client = mongo_factory.get('client')
        self.db = mongo_factory.get('db')
        self.collection = mongo_factory.get('collection')

    def process_item(self, item, spider):
        self.collection.update_one(
            {"id": item["id"]}, {"$set": item}, upsert=True
        )
        return item
