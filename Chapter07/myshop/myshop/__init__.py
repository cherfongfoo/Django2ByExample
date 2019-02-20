# import celery
from .celery import app as celery_app

#pip install eventlet
#celery -A worker -l info -P eventlet