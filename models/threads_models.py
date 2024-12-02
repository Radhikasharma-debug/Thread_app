from pymongo import MongoClient

class ThreadModel:
    def __init__(self, db):
        self.collection = db["threads"]

    def create_thread(self, user_id, content):
        return self.collection.insert_one({"user_id": user_id, "content": content}).inserted_id

    def get_all_threads(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_user_threads(self, user_id):
        return list(self.collection.find({"user_id": user_id}, {"_id": 0}))
