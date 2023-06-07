#!/bin/bash
cd /opt/app/web/

echo "Apply database migrations"
python3.10 manage.py migrate

echo "Starting server"
uwsgi --ini uwsgi.ini
exec "$@"
