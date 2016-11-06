import datetime

from flask import Flask
from flask import request, render_template

from post_writer import insert_post

from models import Post


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        insert_post.delay(text)
        # post = Post(text=text, date_posted=datetime.datetime.now())
        # post.save()

    posts = Post.objects()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
