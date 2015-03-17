import os
basedir = os.path.abspath(os.path.dirname(__file__))

# This is the path of the database file
SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'glocal.db')

# This folder will store the SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

APP_NAME = 'Glocal'
CHOSEN_MEDIA = ['Twitter', 'Instagram', 'Yelp', 'Facebook']

# Security for login/registration pages.
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

