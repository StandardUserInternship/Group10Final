from app import app
from flask import Flask, render_template, forms
from flask_login import LoginManager
from app import views
app.route('/')
def index():
    return render_template('template_file.html', forms=forms)

login=LoginManager(app)
login.login_view

#app.config.from_object('config')