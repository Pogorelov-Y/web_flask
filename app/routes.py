# -*- coding:utf-8 -*-


from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yurii'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
