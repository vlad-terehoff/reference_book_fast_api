#!/bin/sh
MIGRATIONS_PATH="/app/web/alembic/versions"
if [ "$DB_RUN_AUTO_MIGRATE" = "True" ]; then
  if [ -d "$MIGRATIONS_PATH" ] && [ "$(ls -A $MIGRATIONS_PATH)" ]; then
    echo "Running Alembic migrations..."
    alembic upgrade head
  else
    echo "No migration files found in $MIGRATIONS_PATH. Skipping migrations."
  fi
else
  echo "Skipping Alembic migrations due to DB_RUN_AUTO_MIGRATE flag."
fi
gunicorn src.main:app --workers 2 --worker-class src.uvicorn_worker.CustomUvicornWorker --bind=0.0.0.0:8000