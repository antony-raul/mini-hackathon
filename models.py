from app import db


class Post(db.Document):
    descricao = db.StringField(required=True)
    data = db.DateField(required=True)
    crime = db.StringField(required=True)
