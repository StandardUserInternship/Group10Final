from datetime import timezone
from flask import Flask
from flask import render_template, url_for, request, redirect, flash
import flask_login
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import SubmitField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_wtf import FlaskForm
import os
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'dont-touch-my-database'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)  
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__ (self):
        return '<User {}>'.format(self.username)

class Dataset(UserMixin, db.Model):
    set_id= db.Column(db.Integer, primary_key=True)
    set_name= db.Column(db.String(128), index = True, unique =True)
    set_file= db.Column(db.LargeBinary)

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User': User}

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.add(current_user)
        db.session.commit()

@app.route('/', methods=['GET'])
@app.route('/index')
@login_required
def home():
    if not current_user.is_authenticated:
        redirect(url_for('login'))
    return render_template('home.html', title='Home')
        

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #flash messages arent integrated yet.
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('index.html', title='Register', form=form)  


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        User.last_seen.last_seen=datetime.utcnow
        db.session.add(User.last_seen)
        db.session.commit()
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            #flash messages arent integrated yet.
            flash('Invalid username or password')
            return redirect(render_template('index.html'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


if __name__ == "__main__":
    app.run(debug=True)