from datetime import datetime
from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    url_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    postcode = db.Column(db.String(32))
    bookings = db.relationship('Booking', backref='customer', lazy='joined')

    def __repr__(self):
        return '<Customer {}, {}, {}>'.format(self.name, self.email, self.postcode)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    capacity = db.Column(db.Integer)
    bookings = db.relation('Booking', backref='room', lazy='dynamic')

    def check_booked(self, date):
        for booking in self.bookings:
            if (booking.start_date <= date) and (booking.end_date >= date):
                return 1
        else:
            return 0

    def who_booked(self, date):
        for booking in self.bookings:
            if (booking.start_date <= date) and (booking.end_date >= date):
                return Customer.query.get(id=booking.customer_id)
        else:
            return None

    def get_booking(self, date):
        for booking in self.bookings:
            if (booking.start_date <= date) and (booking.end_date >= date):
                return booking
        else:
            return None

    def __repr__(self):
        return '<Room Id: {}, Number: {}, Capacity: {}>'.format(self.id, self.number, self.capacity)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    start_date = db.Column(db.Date, index=True)
    end_date = db.Column(db.Date, index=True)
    length = db.Column(db.Integer, index=True)
    historic = db.Column(db.Boolean)

    def is_historic(self):
        if datetime.today().date() > self.end_date: # If booking was in the past:
            self.historic = True # Set historic flag to True
            return True # Return true

    def __repr__(self):
        return '<Booking Room: {}, Customer: {}, Start: {}, End: {}>'.format(self.room_id, self.customer_id,
                                                                             self.start_date, self.end_date)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bus_name = db.Column(db.String)
    house_name = db.Column(db.String)
    street = db.Column(db.String)
    village = db.Column(db.String)
    maj_town = db.Column(db.String)
    county = db.Column(db.String)
    postcode = db.Column(db.String)
    telephone = db.Column(db.String)

    def __repr__(self):
        return '<Name: {}, House: {}, Street: {}, Village: {}, Town: {}, County: {}, Postcode: {}, Telephone: {}>'\
            .format(self.name, self.house_name, self.street, self.village, self.maj_town, self.county, self.postcode,
                    self.telephone)
