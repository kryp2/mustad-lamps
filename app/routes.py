from flask import render_template
from app import app, board, lamp1
from app.forms import HexForm
from app.arduino import set_hexcolor, set_blink


from pymata4 import pymata4

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/pick_color', methods=['GET', 'POST'])
def hex_color():
    form = HexForm()
    if form.validate_on_submit():
        if form.blink.data == True:
            set_blink(board, lamp1, form.hexcolor.data)
        else:
            set_hexcolor(board, lamp1, form.hexcolor.data)
    return render_template('pick_color.html', title='Fargevelger', form=form)

@app.route('/api/<string:api_hex_color>', methods=['GET', 'POST'])
def hex_color_api(api_hex_color):
    set_hexcolor(board, lamp1, api_hex_color)
    return f'The color is changed to {api_hex_color}'