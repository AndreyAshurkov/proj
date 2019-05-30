from app import db
class Ticket(db.Model):
    from model.client import Client
    from model.flight import Flight
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cost = db.Column(db.Integer,nullable=False)
    client_id= db.Column(db.Integer, db.ForeignKey('client.id'	))
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))
    clientrel = db.relationship(Client, backref="clientrel", cascade='all,delete')
    flightrel = db.relationship(Flight, backref="flightrel", cascade='all,delete')