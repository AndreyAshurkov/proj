from app import db

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    depart = db.Column(db.DateTime, nullable=False)
    arrive = db.Column(db.DateTime, nullable=False)
    pointfrom = db.Column(db.String(30), nullable=False)
    pointto = db.Column(db.String(30), nullable=False)
    airline = db.Column(db.Integer, db.ForeignKey('airline.id'))
    numberseats = db.Column(db.Integer)
    cost = db.Column(db.Integer)
