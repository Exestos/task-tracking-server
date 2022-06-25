heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn time_tracking.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput