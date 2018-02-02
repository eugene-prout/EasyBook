import wtforms
from flask_wtf import FlaskForm


class NewCustomer(FlaskForm):
    name = wtforms.StringField('Name', validators=[wtforms.validators.DataRequired])
    email = wtforms.StringField('Email address', validators=[wtforms.validators.DataRequired()])
    postcode = wtforms.StringField('Postcode', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Create Customer')

class Booking(FlaskForm):
    customer = wtforms.SelectField('Customer', validators=[wtforms.validators.DataRequired()])
    room = wtforms.SelectField('Room', validators=[wtforms.validators.DataRequired()])
    start_date = wtforms.DateField('Start date', validators=[wtforms.validators.DataRequired()])
    end_date = wtforms.DateField('End date', validators=[wtforms.validators.DataRequired()])

class NewRoom(FlaskForm):
    number = wtforms.StringField('Room number', validators=[wtforms.validators.DataRequired()])
    capacity = wtforms.StringField('Room capacity', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Create Room')
