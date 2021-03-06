#!/usr/bin/env bash
# wait-for-postgres.sh

set -e

cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h db --username=docker kv-task -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd