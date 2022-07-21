from flask import Flask
# intiliaze the app

app = Flask(__name__, instance_relative_config=True)

from app import routes

# load the config app

app.config.from_object('config')
from flask_login import LoginManager
# app = Flask(__name__)

login=LoginManager