import os
import pymongo

MONGO_HOST = os.getenv("MONGO_DB_HOST", "mongo_db")
MONGO_PORT = int(os.getenv("MONGO_DB_PORT", 27017))
MONGO_USERNAME = os.getenv("MONGO_DB_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_DB_PASSWORD", "password")
MONGO_CLIENT = pymongo.MongoClient(
    f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
