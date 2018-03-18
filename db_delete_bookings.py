from app import db
from app.models import Booking

bookings = Booking.query.all()
for c in bookings:
    db.session.delete(c)

db.session.commit()
