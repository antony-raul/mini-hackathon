from datetime import datetime
import json
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, url_for, request, redirect
from flask_mongoengine import MongoEngine

from forms import CrimeForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

db = MongoEngine(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from models import Post

    posts = Post.objects
    print(Post.objects)

    if request.method == 'POST':
        hoje = datetime.now()
        p = Post(
            content=request.values['content'],
            descricao=request.values['descricao'],
            data=hoje.strftime("%d/%m/%Y %H:%M"),
            crime=request.values['crime']
        )
        # Salvei tudo no banco
        p.save()
    # Buscando a lista de post
    posts = Post.objects.all()
    return render_template('index.html', titulo="Mini-hackathon", posts=posts)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = CrimeForm(csrf_enabled=False)
    if form.validate_on_submit():
        return 'Formulário enviado com sucesso, por %s/%s/%s' % (
        form.data['descricao'], form.data['data'], form.data['crime'])
    return render_template('contato.html', titulo="crime", form=form)


@app.route('/sobre/')
def sobre():
    return 'Mapa de Crimes'


@app.route('/sobre/<nome>/')
def sobre_autor(nome):
    return 'Esse artigo foi escrito por %s' % nome


if __name__ == '__main__':
    app.run()
