from flask import Flask

# intiliaze the app

app = Flask(__name__, instance_relative_config=True)

from app import views

# load the config app

app.config.from_object('config')