# src/mongodb_handler.py

import pymongo
from config.config import MONGO_URI, DB_NAME, PROFILE_COLLECTION


def get_mongo_client():
    """Create a MongoDB client and return it."""
    return pymongo.MongoClient(MONGO_URI)


def read_profile_attributes(profile_name):
    """Retrieve profile attributes from MongoDB based on profile name."""
    mongo_client = get_mongo_client()
    db = mongo_client[DB_NAME]
    profile = db[PROFILE_COLLECTION].find_one({"profile_name": profile_name})

    if profile:
        #print profile["attributes"]
        return profile["attributes"]
    return None