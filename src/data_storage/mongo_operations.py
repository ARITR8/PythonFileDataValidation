from pymongo import MongoClient
from config.config import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME, PROFILE_COLLECTION


class MongoOperations:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB_NAME]
        self.collection = self.db[MONGO_COLLECTION_NAME]
        self.profiles = self.db[PROFILE_COLLECTION]

    def insert_status_record(self, unique_id, file_name, status):
        record = {
            'unique_id': unique_id,
            'file_name': file_name,
            'status': status
        }
        self.collection.insert_one(record)

    def delete_all_records(self):
        result = self.collection.delete_many({})
        return result.deleted_count

    def read_profile_attributes(self, profile_name):
        profile = self.profiles.find_one({"recordType": profile_name})
        if profile:
            return profile["attributes"]
        return None