from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter correct email.')])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter correct email.')])
    password = PasswordField('Password', validators=[InputRequired()])
    password_confirm = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
