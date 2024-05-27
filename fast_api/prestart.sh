#!/bin/bash

# Wait for MongoDB to be ready
while ! nc -z mongo_db 27017; do
  echo "Waiting for MongoDB..."
  sleep 2
done

# Start the server
exec "$@"