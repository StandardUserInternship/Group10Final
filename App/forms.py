
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError,Email, EqualTo, length,EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired(), length (min=2,max=20)])
        email= StringField("Email", validators=[DataRequired(), Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        confirm_password= PasswordField('Confirmedpassword', validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')


def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
    
    
        