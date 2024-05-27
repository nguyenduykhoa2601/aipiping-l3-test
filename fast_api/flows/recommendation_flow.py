from prefect import flow
from workers.recommendation import call_openai_api, save_to_mongo


@flow
async def recommendation_flow(uid: str, country: str, season: str):
    recommendations = await call_openai_api(country, season)
    await save_to_mongo(uid, country, season, recommendations)
