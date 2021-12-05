
def init():
    from app import db
    db.drop_all()
    from model.admin import Admin
    from model.airline import Airline
    from model.flight import Flight
    from model.client import Client
    from model.ticket import Ticket
    db.create_all()
    admin = Admin(username='admin', password='admin')
    airline1 = Airline(title='Aeroflot')
    airline2 = Airline(title='Ural airlines')
    airline3 = Airline(title='S7 airlines')
    db.session.add(admin)
    db.session.add(airline1)
    db.session.add(airline2)
    db.session.add(airline2)
    db.session.commit()

if __name__ == '__main__':
    init()