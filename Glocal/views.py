from Glocal import app
from flask import render_template, request, flash, redirect
from .forms import RegistrationForm
import collections


def setup_page_dict():
    """Make a dictionary of all the pages in the file for links at the top of
    the web page. Add the name and address of every new page here"""
    page_dict = collections.OrderedDict()
    page_dict['Home'] = '/'
    page_dict['Index'] = '/index'
    page_dict['Registration'] = '/Registration'
    return page_dict


@app.route('/')
def home_page():
    return render_template('home.html', title='Home',
                           page_dict=setup_page_dict(),
                           app_name=app.config['APP_NAME'])


@app.route('/index')
def index_page():
    return render_template('index.html', title='Index',
                           page_dict=setup_page_dict(),
                           chosen_media=app.config['CHOSEN_MEDIA'])


@app.route('/Registration', methods=['GET', 'POST'])
def Registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('The user: {user} was logged in'.format(user=form.username.data))
        return redirect('/')
    return render_template('registration.html', title='Login',
                           page_dict=setup_page_dict(),
                           chosen_media=app.config['CHOSEN_MEDIA'],
                           form=form)
