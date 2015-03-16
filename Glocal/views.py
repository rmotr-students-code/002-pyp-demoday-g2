from Glocal import app
from flask import render_template, request, flash, redirect
from .forms import RegistrationForm
import collections
from Glocal.API import local_tweets
from Glocal.API import local_insta

def setup_page_dict():
    """Make a dictionary of all the pages in the file for links at the top of
    the web page. Add the name and address of every new page here"""
    page_dict = collections.OrderedDict()
    page_dict['Home'] = '/'
    page_dict['Registration'] = '/Registration'
    return page_dict


@app.route('/', methods=['GET','POST'])
def index_page():
    if request.method == 'GET':
        return render_template('home.html', title='Home',
                           page_dict=setup_page_dict(),
                           app_name=app.config['APP_NAME'])

    elif request.method == 'POST':
        st_num = request.form['st_name']
        st_name = request.form['st_num']
        st_type = request.form['st_type']
        city = request.form['city']
        state = request.form['state']
        miles = str(request.form['miles'])
        lst_local_tweets = local_tweets.get_local_tweets(st_num,st_name,st_type,city,state,miles)
        lst_local_insta = local_insta.get_local_instagram(st_num,st_name,st_type,city,state)
        return render_template('results.html', lst_local_tweets = lst_local_tweets, lst_local_insta = lst_local_insta)

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


