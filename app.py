from datetime import datetime
import json
from flask import Flask, render_template, request
from flask_mongoengine import MongoEngine

from forms import CrimeForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from models import Post

    posts = Post.objects
    if request.method == 'POST':

        p = Post(
            descricao=request.values['descricao'],
            data=request.values['data'],
            crime=request.values['crime']
        )
        p.save()
    posts = Post.objects.all()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
