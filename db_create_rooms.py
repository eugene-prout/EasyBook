from app import app, db
from app.models import Customer, Booking, Room

r = Room(number="1", capacity="2")
db.session.add(r)

r = Room(number="2", capacity="3")
db.session.add(r)

r = Room(number="3", capacity="1")
db.session.add(r)

db.session.commit()
