from flask import render_template
from app import app, board, lamp1
from app.forms import ConnectionForm, HexForm, PickColorForm
from app.arduino import set_hexcolor

from pymata4 import pymata4

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/arduino', methods=['GET', 'POST'])
def arduino():
    form = ConnectionForm()
    if form.validate_on_submit():
        print("yes")
    return render_template('arduino.html', title='Arduino', form=form)

@app.route('/pick_color', methods=['GET', 'POST'])
def pick_color():
    form = PickColorForm()
    return render_template('pick_color.html', title='Farge velger', form=form)


@app.route('/hex_color', methods=['GET', 'POST'])
def hex_color():
    form = HexForm()
    if form.validate_on_submit():
        set_hexcolor(board, lamp1, form.hexcolor.data)
    return render_template('hex_color.html', title='Hex Farge', form=form)