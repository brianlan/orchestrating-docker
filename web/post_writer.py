import datetime
import time

from celery import Celery

from models import Post


app = Celery('post_writer', backend='redis://redis:6379/0', broker='amqp://guest@rabbit')


@app.task
def insert_post(text):
    time.sleep(5)
    post = Post(text=text, date_posted=datetime.datetime.now())
    post.save()
    return str(post.id)
