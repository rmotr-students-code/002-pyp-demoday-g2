from flask import Flask
from . import config

app = Flask("myapp")
app.config.from_object(config)
from myapp import views