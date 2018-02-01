from app import db
from app.models import Customer

customers = Customer.query.all()
for c in customers:
    db.session.delete(c)

db.session.commit()
