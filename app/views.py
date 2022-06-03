from . import app
from .FanEnjoyer import FanEnjoyer

from flask import request


@app.route('/')
def index():
    return '<h1 slyle="font-size:1000px">А ну пошёл н*хуй отсюда!!!'


@app.route('/make')
def make():
    fan_text = request.args.get('fan_text')
    enj_text = request.args.get('enj_text')
    obj = FanEnjoyer(fan_text, enj_text)
    res = obj.make()
    return {'result': 'OK' if res == 0 else 'Failed'}

@app.route('/form')
def form():
    return 'Скора будет'
