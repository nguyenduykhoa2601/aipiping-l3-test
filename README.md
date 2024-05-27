# Travel Recommendations API

## Overview

This project is a scalable FastAPI application that provides travel recommendations for a given country and season by leveraging the OpenAI API. The application utilizes Prefect for background processing and MongoDB for storing recommendations. Docker Compose is used to manage the application components.

## Features

- FastAPI endpoint to request travel recommendations.
- Asynchronous background processing using Prefect.
- MongoDB integration for storing and retrieving recommendations.
- Containerized services using Docker Compose.

## Requirements

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```bash
git https://github.com/nguyenduykhoa2601/aipiping-l3-test
cd aipiping-l3-test
```

### 2. Create a .env File

```
FAST_API_PORT=3000
MONGO_DB_HOST=localhost
MONGO_DB_PORT=27017
MONGO_DB_USERNAME=admin
MONGO_DB_PASSWORD=1yfKlEYuZ2pQ3jMYuwKJufMT
OPENAI_API_KEY='YOUR_API_KEY'
PREFECT_PORT=4200
```

### 3. Build and Run the Application

Use Docker Compose to build and run the application:

```bash
docker compose up --build
```

This will start the following services:

fast-api: The FastAPI application.
mongo_db: MongoDB database.
prefect_orion: Prefect Orion service for flow orchestration.
prefect_agent: Prefect agent to run the tasks.

### 4. Access the Application

- FastAPI Documentation: http://localhost:3000/docs
- Prefect Orion UI: http://localhost:4200

### 5. Project Structure

```bash
├── fast_api
│   ├── Dockerfile
│   ├── main.py
│   ├── prestart.sh
│   ├── gunicorn_conf.py
│   ├── helpers
│   │   └── constants.py
│   ├── routes
│   │   └── index.py
│   ├── schemas
│   │   └── recommendation.py
│   ├── flows
│   │   └── recommendation_flow.py
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md

```
