import wtforms
import wtforms.validators
from wtforms import validators, ValidationError
from flask_wtf import FlaskForm
from app import app, db
from app.models import Customer, Room, Booking


class CheckUniqueEmail(object):
    def __init__(self, table, message=None):
        self.table = table
        if not message:
            message = u'A customer is already registered with that email'
        self.message = message

    def __call__(self, form, field):
        e = field.data
        for c in self.table.query.all():
            if c.email == e:
                raise ValidationError(self.message)


class NewCustomer(FlaskForm):
    name = wtforms.StringField('Name', validators=[validators.DataRequired()])
    email = wtforms.StringField('Email address', validators=[validators.DataRequired(), validators.email(),
                                                             CheckUniqueEmail(Customer)])
    postcode = wtforms.StringField('Postcode', validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Create Customer')


class NewBooking(FlaskForm):
    customer = wtforms.SelectField(u'Customer', coerce=int, validators=[validators.DataRequired()])
    room = wtforms.SelectField('Room', coerce=int, validators=[validators.DataRequired()])
    start_date = wtforms.DateField('Start date', format='%d/%m/%Y')
    end_date = wtforms.DateField('End date', format='%d/%m/%Y')
    submit = wtforms.SubmitField('Create Booking')


class NewRoom(FlaskForm):
    number = wtforms.IntegerField('Room number', validators=[validators.DataRequired()])
    capacity = wtforms.IntegerField('Room capacity', validators=[validators.DataRequired(),
                                                                 validators.number_range(min=1)])
    submit = wtforms.SubmitField('Create Room')
