
from flask import Flask, render_template, User,request,url_parse
from flask.cli import shell_command
from app import app 
from flask import flask_shell
from flask_login import login_required
import forms
from flask import  formspassword

from app import current_user, login_user,redirect,url_for,LoginForm, flash
from flask import Flask
import sqlalchemy


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)




@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if forms.validate_on_submit():
        user = User.query.filter_by(username=forms.username.data).first()
        if user is None or not user.check_password(formspassword.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=forms.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')