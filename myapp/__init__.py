from flask import Flask
from . import config

app = Flask("myapp")
app.config.from_object(config)
from myapp import views

# For error logging when debugging is False
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/{}.log'.format(app.config['APP_NAME']),
                                       'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: '
'%(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('{} startup'.format(app.config['APP_NAME']))
