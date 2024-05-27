from pymongo import MongoClient
from pydantic import BaseModel
from uuid import uuid4


class MongoService:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]

    def insert_recommendation(self, uid, country, season, recommendations):
        self.db.recommendations.insert_one({
            "uid": uid,
            "country": country,
            "season": season,
            "recommendations": recommendations,
            "status": "completed"
        })

    def get_recommendation(self, uid):
        return self.db.recommendations.find_one({"uid": uid})
