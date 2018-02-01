from app import db
from app.models import Customer, Booking, Room

c = Customer(name="John", email="john@gmail.com", postcode="SA18 2TA")
db.session.add(c)
r = Room(number="1", capacity="2")
db.session.add(r)

db.session.commit()
b = Booking(customer_id="")
