import openai
from helpers.constants import MONGO_URI, OPENAI_API_KEY
from motor.motor_asyncio import AsyncIOMotorClient
from prefect import task


@task
async def call_openai_api(country: str, season: str) -> list:
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Give me three things to do in {country} during {season}.",
        max_tokens=150
    )
    recommendations = [
        rec.strip() for rec in response.choices[0].text.strip().split("\n") if rec.strip()]

    return recommendations


@task
async def save_to_mongo(uid: str, country: str, season: str, recommendations: list):
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.travel_recommendations
    db.travel_recommendations.update_one(
        {"uid": uid},
        {"$set": {
            "country": country,
            "season": season,
            "recommendations": recommendations,
            "status": "completed"
        }},
        upsert=True
    )
