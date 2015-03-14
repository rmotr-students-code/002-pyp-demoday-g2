from wtforms import TextField, PasswordField, validators, ValidationError
from flask_wtf import Form
from models import User


def check_username_unique(form, username):
    """Checks that the username is not already in the database"""
    if user_in_database(username.data):
        raise ValidationError('\'{}\' already chosen. Please choose another '
                              'username'.format(username.data))


def user_in_database(username):
    if User.query.filter_by(username=username).first():
        return True


class RegistrationForm(Form):
    username = TextField('Username', [validators.length(min=4, max=20,
                        message='Username must be between 4 and 20 characters'),
                                      check_username_unique])

    # Ensures the password contains at least one number and capital letter
    password = PasswordField('Password',
                             [validators.required(),
                              validators.regexp(
                                  r'([a-z]*[A-Z]+\w*\d+)|([a-z]*\d+\w*[A-Z]+)',
                                message='Password must alphanumeric and contain'
                                        ' at least one number and capital letter'
                              )])



