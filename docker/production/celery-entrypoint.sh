#!/bin/bash

set -e

# Wait for PostgreSQL
echo "Waiting for PostgreSQL..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -d "$POSTGRES_DB" -U "$POSTGRES_USER" -c '\q'; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL is up - continuing"

# Wait for Redis
echo "Waiting for Redis..."
until redis-cli -h "$REDIS_HOST" ping | grep PONG; do
  echo "Redis is unavailable - sleeping"
  sleep 1
done
echo "Redis is up - continuing"

# Execute passed command
exec "$@"