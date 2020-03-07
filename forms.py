from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired


class CrimeForm(FlaskForm):
    descricao = StringField('descricao', validators=[DataRequired()])
    data = DateField('data', validators=[DataRequired()])
    crime = StringField('crime', validators=[DataRequired()])
