# -*- coding:utf-8 -*-


from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yurii'}
    return render_template('index.html', title='Home', user=user)
