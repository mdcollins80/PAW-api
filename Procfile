web: gunicorn config.wsgi:application
worker: celery worker --app=paw2018.taskapp --loglevel=info
