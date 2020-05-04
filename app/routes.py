# -*- coding:utf-8 -*-


from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yurii'}
    posts = [
        {
            'author':{'username': 'Susan'},
            'body': 'Beautiful day'
        },
        {
            'author':{'username': 'Evgen'},
            'body': 'Vipiem!'
        },
        {
            'author':{'username': 'Samokat'},
            'body': 'O-o-o-a-a-a'
        }
]
    return render_template('index.html', title='Home', user=user, posts=posts)
