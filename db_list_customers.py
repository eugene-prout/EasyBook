from app import db
from app.models import Customer

c = Customer.query.all()

for customer in c:
    print(customer)