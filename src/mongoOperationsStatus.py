from pymongo import MongoClient

import pymongo
from config import MONGO_URI


def get_mongo_client():
    """Create a MongoDB client and return it."""
    return pymongo.MongoClient(MONGO_URI)


client = MongoClient('mongodb://localhost:27017')
db = client['MyDatabase']
   # db = get_mongo_client()[]
collection = db["StatusCollection"]

def insert_status_record(unique_id, file_name, status):
    """Insert a record into the MongoDB collection."""
    record = {
        'unique_id': unique_id,
        'file_name': file_name,
        'status': status
    }
    collection.insert_one(record)

def delete_all_records():
    """Delete all records from the MongoDB collection."""
    result = collection.delete_many({})  # The empty filter {} matches all documents
    print(f"Deleted {result.deleted_count} records from the collection.")