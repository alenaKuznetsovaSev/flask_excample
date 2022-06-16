from flask import render_template
from app import app


# home page
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alen'}
    posts = [
        {
            'author': {'username': 'Max'},
            'body': 'Hello everybody!'
        },
        {
            'author': {'username': 'Lily'},
            'body': 'HI!'
        }
    ]
    page = render_template('index.html', title='Home', user=user, posts=posts)
    return page
