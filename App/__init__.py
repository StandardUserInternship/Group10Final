from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app import routes 
# intiliaze the app

app = Flask(__name__, instance_relative_config=True)

from flask import views

# load the config app


app.config.from_object(Config)
db = SQLAlchemy(app)
from flask_login import LoginManager


login=LoginManager
