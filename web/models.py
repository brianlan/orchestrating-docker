from mongoengine import *


connect(host='localhost', port=27017, name='orchestrating_docker')


class Post(Document):
    text = StringField(required=True)
    date_posted = DateTimeField(required=True)
