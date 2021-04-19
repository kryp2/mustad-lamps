from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ConnectionForm(FlaskForm):
    submit = SubmitField('Open')

class HexForm(FlaskForm):
    hexcolor = StringField('Hex verdi', validators=[DataRequired()])
    submit = SubmitField('Bytt farge')

class PickColorForm(FlaskForm):
    red = SubmitField('Red')
    ntnublue = SubmitField('NTNU Blue')
