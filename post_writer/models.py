from mongoengine import *


connect('orchestrating_docker', host='mongodb', port=27017, connect=False)


class Post(Document):
    text = StringField(required=True)
    date_posted = DateTimeField(required=True)
