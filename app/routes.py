import sqlalchemy
from flask import render_template, request, url_for, redirect, session
from wtforms import Form, StringField, validators
from app import app, db
from app.models import Customer, Room, Booking
from app.forms import NewCustomer


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home', customers=Customer.query.all())


@app.route('/all_customers')
def all_customers():
    return render_template('all_customers.html', customers=Customer.query.all())


@app.route('/new_customer', methods=['GET', 'POST'])
def new_customers():
    if request.method == 'POST':
        #try:
        name_url = request.form['name'].replace(' ', '_')
        c = Customer(name=request.form['name'], url_name=name_url, email=request.form['email'],
                     postcode=request.form['postcode'])
        db.session.add(c)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('index'))
        #except sqlalchemy.exc.IntegrityError as err:
        #return render_template('new_customer.html')
    return render_template('new_customer.html')


@app.route('/new_room', methods=['GET', 'POST'])
def new_room():
    if request.method == 'POST':
        r = Room(number=request.form['number'], capacity=request.form['capacity'])
        db.session.add(r)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_room.html')


@app.route('/view_rooms')
def view_rooms():
    return render_template('all_rooms.html', rooms=Room.query.all())


@app.route('/room/<id>', methods=['GET', 'POST'])
def room(id):
    _room = Room.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        db.session.delete(_room)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('view_room.html', room=_room)


@app.route('/customer/<url_name>', methods=['GET', 'POST'])
def customer(url_name):
    _customer = Customer.query.filter_by(url_name=url_name).first_or_404()
    if request.method == 'POST':

        #if request.form['name'] == _customer.name:

        db.session.delete(_customer)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('index'))
        # #else:
        #     return render_template('customer.html', customer=_customer,
        #                            error="Please type customer's name into box to delete")

    return render_template('customer.html', customer=_customer)


@app.route('/booking/new', methods=['GET', 'POST'])
def new_booking():
    if request.method == 'POST':
        print(request.form['customer'])
        return redirect(url_for('index'))
    return render_template('new_booking.html', customers=Customer.query.all(), rooms=Room.query.all())


@app.route('/all_bookings')
def all_bookings():
    return render_template('bookings.html', bookings=Booking.query.all())

@app.route('/test')
def test():
    return render_template('test.html')
