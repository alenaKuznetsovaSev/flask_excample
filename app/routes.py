from flask import render_template
from app import app


# home page
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alen'}
    page = render_template('index.html', title='Home', user= user)
    return page
