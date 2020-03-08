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
    # Abri o arquivo de posts
    f = open('posts.json', 'r')
    # Converti o texto em lista
    posts: object = json.loads(f.read())
    # Quando chamou o POST para salvar um novo arquivo
#   posts = Post.objects
    if request.method == 'POST':

        hoje = datetime.now()
        posts.append(
            descricao=request.values['descricao'],
            data=hoje.strftime("%d/%m/%Y %H:%M"),
            crime=request.values['crime']
        )
        # Salvei tudo no banco
        f = open('posts.json', 'w')
        f.write(json.dumps(posts))
        f.close()
#        p.save()
#    posts = Post.objects.all()
    return render_template('index.html', titulo="Mini-hackathon", posts=posts)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = CrimeForm(csrf_enabled=False)
    if form.validate_on_submit():
        return 'Formulário enviado com sucesso, por %s/%s' % (form.data['descricao'], form.data['data'], form.data['crime'])
    return render_template('contato.html', titulo="crime", form=form)


#if __name__ == '__main__':
#    app.run()