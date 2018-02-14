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

class CheckDateOrder(object):
    def __int__(self, message=None):
        if not message:
            message = u'Please select a departure date after the arrival date'


class DeleteCustomer(FlaskForm):
    nameCheck = wtforms.StringField('Please enter customer name to delete',
                                    validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Delete Customer')


class DeleteRoom(FlaskForm):
    roomNumber = wtforms.IntegerField('Please enter room number to delete',
                                      validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Delete Room')


class DeleteBooking(FlaskForm):
    bookingNumber = wtforms.IntegerField('Please enter booking number to delete',
                                   validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Delete Booking')


class NewCustomer(FlaskForm):
    name = wtforms.StringField('Name', validators=[validators.DataRequired()])
    email = wtforms.StringField('Email address', validators=[validators.DataRequired(), validators.email(),
                                                             CheckUniqueEmail(Customer)])
    postcode = wtforms.StringField('Postcode', validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Create Customer')


class NewBooking(FlaskForm):
    customer = wtforms.SelectField(u'Customer', coerce=int, validators=[validators.DataRequired()])
    room = wtforms.SelectField('Room', coerce=int, validators=[validators.DataRequired()])
    start_date = wtforms.DateField('Arrival date', format='%d/%m/%Y')
    end_date = wtforms.DateField('Departure date', format='%d/%m/%Y')
    submit = wtforms.SubmitField('Create Booking')


class SelectBooking(FlaskForm):
    booking = wtforms.SelectField(u'Booking', coerce=int, validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Select booking')


class SelectCustomer(FlaskForm):
    customer = wtforms.SelectField(u'Customer name', coerce=int, validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Select customer')


class SelectRoom(FlaskForm):
    room = wtforms.SelectField(u'Room number', coerce=int, validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Select room')



class ChangeBooking(FlaskForm):
    customer = wtforms.SelectField(u'Customer', coerce=int, validators=[validators.DataRequired()])
    room = wtforms.SelectField(u'Room', coerce=int, validators=[validators.DataRequired()])
    start_date = wtforms.DateField('Arrival date', format='%d/%m/%Y', validators=[validators.DataRequired()])
    end_date = wtforms.DateField('Departure date', format='%d/%m/%Y', validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Change booking')


class NewRoom(FlaskForm):
    number = wtforms.IntegerField('Room number',
                                  validators=[validators.DataRequired(),
                                              validators.number_range(min=1, message="Room number must be above 1")], placeholder="Arrival date")
    capacity = wtforms.IntegerField('Room capacity',
                                    validators=[validators.DataRequired(),
                                                validators.number_range(min=1, message="Capacity must be above 1")])
    submit = wtforms.SubmitField('Create Room')


class GetCost(FlaskForm):
    cost = wtforms.DecimalField('Cost per night', validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Select booking')
