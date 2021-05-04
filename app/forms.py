from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, Form
from wtforms.validators import DataRequired

class HexForm(FlaskForm):
    hexcolor = StringField('Hex verdi', validators=[DataRequired()], id='color', default='#00509e')
    submit = SubmitField('Bytt farge')
    blink = BooleanField('Blink')


