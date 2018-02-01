from datetime import datetime
from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    url_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    postcode = db.Column(db.String(32))
    bookings = db.relationship('Booking', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer {}, {}, {}>'.format(self.name, self.email, self.postcode)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    capacity = db.Column(db.Integer)
    booking = db.relation('Booking', backref='room', lazy='dynamic')

    def __repr__(self):
        return '<Room Id: {}, Number: {}, Capacity: {}>'.format(self.id, self.number, self.capacity)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    start_date = db.Column(db.DateTime, index=True)
    end_date = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Booking Room: {}, Customer: {}, Start: {}, End: {}>'.format(self.room_id, self.customer_id,
                                                                             self.start_date, self.end_date)
