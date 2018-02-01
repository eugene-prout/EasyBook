from app import db
from app.models import Customer, Room, Booking
from datetime import datetime

c = Customer(name="John Smith", email="john@gmail.com", postcode="SA67 8NS")
db.session.add(c)
print("Added customer")

r = Room(number=1, capacity=2)
db.session.add(r)
print("Added room")

_customer = Customer.query.filter_by(name="John Smith").first_or_404()
_room = Room.query.filter_by(number=1).first_or_404()
start_date = datetime.strptime('12/02/18', "%d/%m/%y")
end_date = datetime.strptime('13/02/18', "%d/%m/%y")

b = Booking(customer_id=_customer.id, room_id=_room.id, start_date=start_date, end_date=end_date)
db.session.add(b)
print("Added booking")

db.session.commit()
