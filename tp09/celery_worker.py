from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")
# celery -A celery_worker worker --loglevel=info -P solo

@app.task
def hello():
    return 'hello world'