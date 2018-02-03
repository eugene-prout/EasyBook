import wtforms
from flask_wtf import FlaskForm


class NewCustomer(FlaskForm):
    name = wtforms.StringField('Name', validators=[wtforms.validators.DataRequired])
    email = wtforms.StringField('Email address', validators=[wtforms.validators.DataRequired()])
    postcode = wtforms.StringField('Postcode', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Create Customer')


class NewBooking(FlaskForm):
    customer = wtforms.SelectField(u'Customer', coerce=int, validators=[wtforms.validators.DataRequired()])
    room = wtforms.SelectField('Room', coerce=int, validators=[wtforms.validators.DataRequired()])
    start_date = wtforms.DateField('Start date', format='%d/%m/%Y')
    end_date = wtforms.DateField('End date', format='%d/%m/%Y')
    submit = wtforms.SubmitField('Create Booking')


class NewRoom(FlaskForm):
    number = wtforms.StringField('Room number', validators=[wtforms.validators.DataRequired()])
    capacity = wtforms.StringField('Room capacity', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Create Room')
