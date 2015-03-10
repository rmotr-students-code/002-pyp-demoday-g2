from myapp import app
from flask import render_template

app_name = app.config['APP_NAME']
chosen_media = app.config['CHOSEN_MEDIA']

# Add the name and link for each page we make to this. They will automatically
# be added to the links at the top. Need to find a way to order them
page_dict = {}

@app.route('/')
def home_page():
    page_dict['Home'] = '/'
    return render_template('home.html', title='Home', page_dict=page_dict,
                           app_name=app_name)

@app.route('/index')
def index_page():
    page_dict['Index'] = '/index'
    return render_template('index.html', title='Index', page_dict=page_dict,
                           chosen_media=chosen_media)

# @app.route('/Login')
# def login():
#     return

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