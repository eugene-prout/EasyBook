from flask_wtf import FlaskForm, validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewCustomer(FlaskForm):
    name = StringField('Customer name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    postcode = StringField('Postcode', validators=[DataRequired()])
