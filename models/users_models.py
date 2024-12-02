class UserModel:
    def __init__(self, db):
        self.collection = db["users"]

    def create_user(self, username):
        return self.collection.insert_one({"username": username}).inserted_id

    def get_user(self, username):
        return self.collection.find_one({"username": username}, {"_id": 0})
