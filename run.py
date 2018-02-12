from app import app, db
from app.models import Customer, Room, Booking
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

local = input("Run server over network? ").lower()
if local in ['y', 'yes']:
    print("Running over network")
    app.run(host="0.0.0.0")
else:
    print("Running locally")
    app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Customer=Customer, Room=Room, Booking=Booking)