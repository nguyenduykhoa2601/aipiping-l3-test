from pydantic import BaseModel, constr
from typing import List


class RequestModel(BaseModel):
    country: str
    season: constr(pattern='^(spring|summer|fall|winter)$')


class RecommendationModel(BaseModel):
    uid: str
    country: str
    season: str
    recommendations: List[str]
    status: str
