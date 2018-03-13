from app import db
from app.models import Room

room = Room.query.all()
for r in room:
    if r.id > 15:
        for booking in r.bookings:
            db.session.delete(booking)
        db.session.delete(r)

db.session.commit()
