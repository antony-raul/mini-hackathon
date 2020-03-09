from app import db

class Post(db.Document):
    content = db.StringField(required=True)
    descricao = db.StringField(required=True)
    data = db.DateField(required=True)
    crime = db.StringField(required=True)

    def __str__(self):
        return self.content