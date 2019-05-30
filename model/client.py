from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def get_username(self):
        return self.username

    def checkPas(self, pas):
        return self.password == pas
