from wtforms import TextField, PasswordField, BooleanField, validators
from flask_wtf import Form


class RegistrationForm(Form):
    username = TextField('Username', [validators.length(min=4, max=20,
                        message='Username must be between 4 and 20 characters')]
    )
    # Ensures the password contains at least one number and capital letter
    password = PasswordField('Password',
                             [validators.required(),
                              validators.regexp(
                                  r'([a-z]*[A-Z]+\w*\d+)|([a-z]*\d+\w*[A-Z]+)',
                                message='Password must alphanumeric and contain'
                                        'at least one number and capital letter'
                              )])
    remember_me = BooleanField('Remember Me')


