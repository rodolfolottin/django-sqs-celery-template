#!/bin/bash
set -e

if [ -n "$1" ]; then
    exec "$@"
fi

mkdir -p /usr/src/logs

# Prepare log files and start outputting logs to stdout
touch /usr/src/logs/gunicorn.log
touch /usr/src/logs/access.log
tail -n 0 -f /usr/src/logs/*.log &


python docker/web/check_db.py --service-name Postgres --ip db --port 5432

python src/manage.py migrate
python src/manage.py collectstatic --noinput  # Collect static files

echo Starting Gunicorn.
if [ "$ENV" = "development" ] ; then
    (cd src; exec gunicorn --reload app.wsgi --bind 0.0.0.0:8000)
else
    (cd src; exec gunicorn app.wsgi \
         --name core \
         --bind 0.0.0.0:8000 \
         --workers 3 \
         --timeout 120 \
         --worker-class gevent \
         --log-level=info \
         --log-file=/usr/src/logs/gunicorn.log \
         --access-logfile=/usr/src/logs/access.log \
         "$@")
fi
