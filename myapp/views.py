from myapp import app
from flask import render_template
import collections

app_name = app.config['APP_NAME']
chosen_media = app.config['CHOSEN_MEDIA']

def setup_page_dict():
    """Make a dictionary of all the pages in the file for links at the top of
    the web page. Add the name and address of every new page here"""
    page_dict = collections.OrderedDict()
    page_dict['Home'] = '/'
    page_dict['Index'] = '/index'
    page_dict['Login'] = 'Login'
    return page_dict

@app.route('/')
def home_page():
    return render_template('home.html', title='Home',
                           page_dict=setup_page_dict(),
                           app_name=app_name)

@app.route('/index')
def index_page():
    return render_template('index.html', title='Index',
                           page_dict=setup_page_dict(),
                           chosen_media=chosen_media)

@app.route('/Login')
def login():
    return render_template('login.html', title='Login',
                           page_dict=setup_page_dict(),
                           chosen_media=chosen_media)

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