from app import app, db
from app.models import Customer, Room, Booking

try:
    app.run(host="0.0.0.0")
except KeyboardInterrupt:
    quit()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Customer': Customer, 'Room': Room, 'Booking': Booking}