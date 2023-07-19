#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 source/manage.py flush --no-input
python3 source/manage.py migrate
python3 source/manage.py collectstatic

exec "$@"