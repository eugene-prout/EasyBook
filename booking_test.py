from app import app, db
from app.models import Customer, Booking, Room
import datetime

b = Room.query.filter_by(number=2).first()

today = datetime.datetime.strptime('11/02/2018', '%d/%m/%Y').date()
x = b.check_booked(today)

print(x)
