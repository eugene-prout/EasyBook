from app import db
from app.models import Customer, Room, Booking
import names
import random
import string
import datetime

#TODO: build brute force model



def cust(number):
    for x in range(number):
        name = names.get_full_name()
        name_url = name.replace(' ', '_')
        email = name_url + "@mail.com"
        postcode = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))

        c = Customer(name=name, url_name=name_url, email=email, postcode=postcode)

        db.session.add(c)
        db.session.commit()
        print(x)


def room(number):
    for x in range(number):
        r = Room(number=x, capacity=random.randint(1, 5))
        db.session.add(r)
        db.session.commit()


def booking(number, _rooms, _customers, all_bookings):

    today = datetime.datetime.today().date()
    start = today + datetime.timedelta(days=-3)
    end = today + datetime.timedelta(days=2)
    length = (end - start).days

    count = 0
    for r in _rooms:
        c = random.choice(_customers)
        _customers.remove(c)
        count += 1
        _booking = Booking(customer_id=c.id, room_id=r.id, start_date=start,
                           end_date=end, length=length)
        db.session.add(_booking)
        db.session.commit()
        if count > number:
            break
        print(count)

"""
for c in customers:
    db.session.delete(c)

for r in rooms:
    db.session.delete(r)
    
for b in bookings:
    db.session.delete(b)
    

"""
customers = Customer.query.all()
rooms = Room.query.all()
bookings = Booking.query.all()

booking(95, rooms, customers, bookings)

db.session.commit()
