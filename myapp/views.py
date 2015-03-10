from myapp import app
from flask import render_template

app_name = app.config['APP_NAME']

@app.route('/')
def home_page():
    return render_template('home.html', title='Home', app_name=app_name)

@app.route('/index')
def index_page():
    return render_template('index.html', title='Index', app_name=app_name)

# When debugging is set to off, these pages will show when the respective errors
# are raised
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='Error 404', app_name=app_name), \
           404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title='Error 500', app_name=app_name), \
           500