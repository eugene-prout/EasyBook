from app import app, db
from app.models import Customer, Room, Booking
import logging
import random, threading, webbrowser
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import socket

print(socket.gethostbyname(socket.gethostname()))

#threading.Timer(1.25, lambda: webbrowser.open("http://{}:5000".format(socket.gethostbyname(socket.gethostname())))).start()
#app.run(host="0.0.0.0", port=5000)

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