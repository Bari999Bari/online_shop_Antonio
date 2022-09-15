# import celery
from .celery import app as celery_app
# celery -A myshop worker -l info -P gevent