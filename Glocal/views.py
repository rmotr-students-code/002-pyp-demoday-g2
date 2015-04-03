from Glocal import app
from flask import render_template, request
import collections
from Glocal.API import API

def setup_page_dict():
    """Make a dictionary of all the pages in the file for links at the top of
    the web page. Add the name and address of every new page here"""
    page_dict = collections.OrderedDict()
    page_dict['Home'] = '/'
<<<<<<< HEAD
=======
    page_dict['Registration'] = '/Registration'
    page_dict['Contact'] = '/Contact'
>>>>>>> MRA
    return page_dict

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('home.html', title='Home',
                               page_dict=setup_page_dict(),
                               app_name=app.config['APP_NAME'])

    elif request.method == 'POST':
        st_address = request.form['st_address']
        city = request.form['city']
        state = request.form['state']
        miles = request.form['miles']
        user_query = API.GlocalAPI(st_address, city, state, miles)
        lst_local_tweets, lst_trending_tweets = user_query.get_twitter()
        lst_local_insta = user_query.get_instagram()
        lst_four_square_trending, lst_four_square_explore = user_query.get_four_square()
        lst_events = user_query.get_events()
        return render_template('results.html', title='Home',
                               page_dict=setup_page_dict(),
                               app_name=app.config['APP_NAME'],
                               lst_local_tweets=lst_local_tweets,
<<<<<<< HEAD
                               lst_trending_tweets=lst_trending_tweets,
                               lst_local_insta=lst_local_insta,
                               lst_four_square_trending=lst_four_square_trending,
                               lst_four_square_explore=lst_four_square_explore,
                               lst_events = lst_events,
                               st_address = st_address,
                               city = city,
                               state = state)
=======
                               lst_local_insta=lst_local_insta,
                               st_address = st_address,
                               city = city,
                               state = state)

@app.route('/Registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        add_to_database(form.username.data, form.password.data,
                        form.first_name.data, form.last_name.data)
        flash('Welcome {first_name}!'.format(first_name=form.first_name.data))
        return redirect('/')
    return render_template('registration.html', title='Registration',
                           page_dict=setup_page_dict(),
                           chosen_media=app.config['CHOSEN_MEDIA'],
                           form=form)


>>>>>>> MRA
