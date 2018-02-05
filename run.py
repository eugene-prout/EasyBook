from app import app, db
from app.models import Customer, Room, Booking

#app.run(host="0.0.0.0")


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Customer=Customer, Room=Room, Booking=Booking)