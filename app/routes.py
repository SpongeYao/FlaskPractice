from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ying'}
    posts = [
        {
            'author': {'username': 'dkwolf'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'MingXi Hsieh'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
