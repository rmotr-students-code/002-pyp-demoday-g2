from myapp import app
from flask import render_template

app_name = app.config['APP_NAME']

@app.route('/')
def home_page():
    return render_template('home.html', title='Home', app_name=app_name)

@app.route('/index')
def index_page():
    return render_template('index.html', title='Index', app_name=app_name)