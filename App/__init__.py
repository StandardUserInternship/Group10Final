from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db= SQLAlchemy(app)
migrate=Migrate(app, db)
from app import routes, models
from flask_login import LoginManager
app= Flask(__name__)
login = LoginManager(app)

app= Flask(__name__, instance_relative_config=True)


from app import routes

app.config.from_object('config')




login=LoginManager(app)
login.login_view='login'



