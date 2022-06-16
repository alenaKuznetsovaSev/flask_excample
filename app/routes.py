from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # receiving login request
        flash(f'Login request form user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    # login page
    return render_template('login.html', title='Sing In', form=form)

