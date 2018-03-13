import flask
import sqlalchemy
from flask import render_template, request, url_for, redirect, session
from wtforms import Form, StringField, validators
from app import app, db
from app.models import Customer, Room, Booking
from app.forms import NewCustomer, NewRoom, NewBooking, DeleteCustomer, DeleteRoom, DeleteBooking, ChangeBooking
import datetime
import calendar

#TODO: add ability to update database fields

def check_clash(room, date):
    if room.check_booked(date):
        return True

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', customers=Customer.query.all())


@app.route('/all_customers')
def all_customers():
    return render_template('all_customers.html', customers=Customer.query.all())


@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    form = NewCustomer()

    if form.validate_on_submit():
        name_url = form.name.data.replace(' ', '_')
        c = Customer(name=form.name.data, url_name=name_url, email=form.email.data,
                     postcode=form.postcode.data)

        db.session.add(c)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_customer.html', form=form)


@app.route('/new_room', methods=['GET', 'POST'])
def new_room():
    form = NewRoom()
    if form.validate_on_submit():
        r = Room(number=form.number.data, capacity=form.capacity.data)
        db.session.add(r)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('view_rooms'))

    return render_template('new_room.html', form=form)


@app.route('/view_rooms')
def view_rooms():
    return render_template('all_rooms.html', rooms=Room.query.all())


@app.route('/room/<id>', methods=['GET', 'POST'])
def room(id):
    _room = Room.query.filter_by(id=id).first_or_404()
    form = DeleteRoom()

    if form.validate_on_submit():
        if form.roomNumber.data == _room.number:
            for b in _room.booking.all():
                db.session.delete(b)
            db.session.delete(_room)
            db.session.flush()
            db.session.commit()
            return redirect(url_for('view_rooms'))
        else:
            return render_template('view_room.html', room=_room, form=form, confirm=True)

    return render_template('view_room.html', room=_room, form=form, confirm=False)


@app.route('/customer/<url_name>', methods=['GET', 'POST'])
def customer(url_name):
    _customer = Customer.query.filter_by(url_name=url_name).first_or_404()
    form = DeleteCustomer()

    if form.validate_on_submit():
        if form.nameCheck.data == _customer.name:

            for b in _customer.bookings.all():
                db.session.delete(b)
            db.session.delete(_customer)
            db.session.flush()
            db.session.commit()

            return redirect(url_for('all_customers'))
        else:
            return render_template('customer.html', customer=_customer, form=form, confirm=True)

    return render_template('customer.html', customer=_customer, form=form, confirm=False)


@app.route('/booking/new', methods=['GET', 'POST'])
def new_booking():
    form = NewBooking(request.form)
    form.customer.choices = [(c.id, c.name) for c in Customer.query.order_by('name')]
    form.room.choices = [(r.id, r.number) for r in Room.query.order_by('number')]

    if form.validate_on_submit():
        start_date = datetime.datetime.strftime(datetime.datetime.strptime(str(form.start_date.data), '%Y-%m-%d'), '%d/%m/%Y')
        start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        start_date = datetime.datetime.date(start_date)

        end_date = datetime.datetime.strftime(datetime.datetime.strptime(str(form.end_date.data), '%Y-%m-%d'), '%d/%m/%Y')
        end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        end_date = datetime.datetime.date(end_date)

        length = (end_date - start_date).days

        _room = Room.query.filter_by(id=form.room.data).first()

        dates_of_booking = [start_date + datetime.timedelta(x) for x in range(length)]

        for date in dates_of_booking:
            if _room.check_booked(date):
                print('Overlapped bookings')
                return render_template('new_booking.html', form=form, error="This booking overlaps with another.")

        _booking = Booking(customer_id=form.customer.data, room_id=form.room.data, start_date=start_date, end_date=end_date, length=length)

        db.session.add(_booking)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('all_bookings'))

    return render_template('new_booking.html', form=form)


@app.route('/all_bookings')
def all_bookings():
    return render_template('bookings.html', bookings=Booking.query.all())


@app.route('/booking/<id>', methods=['GET', 'POST'])
def booking(id):
    _booking = Booking.query.filter_by(id=id).first_or_404()
    form = DeleteBooking()

    if form.validate_on_submit():
        if form.bookingNumber.data == _booking.id:
            db.session.delete(_booking)
            db.session.flush()
            db.session.commit()

            return redirect(url_for('all_bookings'))
        else:
            return render_template('booking.html', booking=_booking, form=form, confirm=True)
    return render_template('booking.html', booking=_booking, form=form, confirm=False)


@app.route('/booking/week', methods=['GET', 'POST'])
def week_book():
    all_rooms = Room.query.all()

    try:
        today = datetime.datetime.strptime(request.args.getlist('link')[0], '%Y-%m-%d').date()
    except IndexError:
        today = datetime.datetime.today().date()

    day = today.weekday()
    start_of_week = today - datetime.timedelta(days=day) # Date object of start of week

    dates_of_week = [start_of_week + datetime.timedelta(x) for x in range(7)]

    next_week = dates_of_week[6] + datetime.timedelta(days=1)
    previous = dates_of_week[0] - datetime.timedelta(days=1)

    return render_template('bookings_week.html', rooms=all_rooms, date_list=dates_of_week, prev=previous, next=next_week)


@app.route('/booking/month', methods=['GET', 'POST'])
def month_book():
    all_rooms = Room.query.all()

    try:
        today = datetime.datetime.strptime(request.args.getlist('link')[0], '%Y-%m-%d').date()
        year = today.year
        month = today.month
    except IndexError:
        today = datetime.datetime.today().date()
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month

    num_days = calendar.monthrange(year, month)[1]
    day = today.weekday()

    dates_of_month = [datetime.date(year, month, day) for day in range(1, num_days+1)]

    next_week = dates_of_month[num_days-1] + datetime.timedelta(days=1)
    print(next_week)
    previous = dates_of_month[0] - datetime.timedelta(days=1)
    print(previous)

    return render_template('monthly_bookings.html', rooms=all_rooms, date_list=dates_of_month, prev=previous, next=next_week)


@app.route('/booking/modify/<id>', method=['GET', 'POST'])
def change_book(id):
    _booking = Booking.query.filter_by(id=id).first_or_404()
    form = ChangeBooking()
    form.customer.choices = [(c.id, c.name) for c in Customer.query.order_by('name')]
    form.room.choices = [(r.id, r.number) for r in Room.query.order_by('number')]

    if form.validate_on_submit():
        if form.customer.data is not None:
            _booking.customer = form.customer.data
        else:
            _booking.customer = form.customer.data

        if form.room.data is not None:
            _booking.room = form.room.data
        else:
            _booking.room = form.room.data

        return redirect(url_for('booking', id=_booking.id))


@app.route('/test')
def test():
    return render_template('test.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
