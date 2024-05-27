from routes.index import routerRecommendation
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=routerRecommendation)


@app.get("/")
async def root():
    return {
        "app": "L3 Test"
    }
