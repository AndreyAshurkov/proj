from app import db


class Airline(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), unique=True, nullable=False)


