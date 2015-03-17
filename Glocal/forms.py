from wtforms import TextField, PasswordField, BooleanField, validators
from flask_wtf import Form
from models import User
import re


def check_unique(form, field):
    """Checks that the username is not already in the database"""
    if user_in_database(field.data):
        raise ValidationError('\'{}\' already chosen. Please choose another '
                              'Username'.format(field.data))


def user_in_database(username):
    return User.query.filter_by(username=username).first()


def letters_only(form, name):
    """Checks that field only contains letters"""
    if not re.search(r'^[a-zA-Z]*$', name.data):
        raise ValidationError('Name must only contain letters.')


class RegistrationForm(Form):
    username = TextField('Username', [validators.length(min=4, max=20,
                        message='Username must be between 4 and 20 characters'),
                                      check_unique])

    # Ensures the password contains at least one number and capital letter
    password = PasswordField('Password',
                             [validators.required(),
                              validators.regexp(
                                  r'([a-z]*[A-Z]+\w*\d+)|([a-z]*\d+\w*[A-Z]+)',
                                message='Password must alphanumeric and contain'
                                        'at least one number and capital letter'
                              )])

    first_name = TextField('First name',
                           [validators.required(message='Please enter your first'
                                                        'name'), letters_only])

    last_name = TextField('Last name',
                          [validators.required(message='Please enter your last'
                                                       'name'), letters_only])
