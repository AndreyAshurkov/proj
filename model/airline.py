from app import db


class Airline(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), unique=True, nullable=False)

    def get_username(self):
        return self.username

    def checkPas(self, pas):
        return self.password == pas
