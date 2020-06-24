from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'KaRUN'}
    posts = [
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Gerry'},
            'body': 'I love basketball!'
        },
        {
            'author':{'username':'Christopher'},
            'body': 'I want Chik-Fil-A!'
        }
        
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)




