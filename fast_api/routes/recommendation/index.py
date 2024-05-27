
from uuid import uuid4
from fastapi import HTTPException
from helpers.constants import MONGO_URI
from routes.index import routerRecommendation as router
from schemas.recommendation import RequestModel
from flows.recommendation_flow import recommendation_flow
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URI)
db = client.travel_recommendations


@router.post("/recommendations", response_model=dict)
async def get_recommendations(request: RequestModel):
    uid = str(uuid4())
    await db.travel_recommendations.insert_one(
        {"uid": uid, "country": request.country, "season": request.season, "status": "pending"})
    asyncio.create_task(recommendation_flow(
        uid=uid, country=request.country, season=request.season))
    return {"uid": uid}


@router.get("/recommendations/{uid}", response_model=dict)
async def get_recommendation_status(uid: str):
    recommendation = await db.travel_recommendations.find_one({"uid": uid})
    if not recommendation:
        raise HTTPException(status_code=404, detail="UID not found")
    if recommendation['status'] == 'pending':
        return {"uid": uid, "status": "pending", "message": "The recommendations are not yet available. Please try again later."}
    elif recommendation['status'] == 'completed':
        return {
            "uid": uid,
            "country": recommendation["country"],
            "season": recommendation["season"],
            "recommendations": recommendation["recommendations"],
            "status": "completed"
        }
    raise HTTPException(
        status_code=500, detail="Unexpected status in database")
