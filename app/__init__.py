from flask import Flask
from pymata4 import pymata4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
board = pymata4.Pymata4()
lamp1 = (9, 10, 11) # (R, G, B)

from app import routes
