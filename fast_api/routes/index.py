from fastapi import APIRouter

routerRecommendation = APIRouter(tags=["recommendation"])

from routes.recommendation.index import *
