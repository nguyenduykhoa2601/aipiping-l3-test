# fast_api/Dockerfile
FROM python:3.8-slim

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
WORKDIR /fast_api
COPY requirements.txt /fast_api/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /fast_api

# Set the entrypoint
ENTRYPOINT ["/fast_api/prestart.sh"]
