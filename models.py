from app import db

class Post(db.Document):

    descricao = db.StringField(required=True)
    data = db.StringField(required=True)
    crime = db.StringField(required=True)

