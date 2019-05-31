from flask import Blueprint, request, render_template, redirect, session

mod = Blueprint('changeTicket', __name__)
from app import db
from model.flight import Flight
from model.client import Client
from model.ticket import Ticket


@mod.route('/mytickets', methods=['GET'])
def mytickets():
    client = Client.query.filter_by(username=session['name']).one()
    query = db.session.query(Ticket,Flight).filter_by(client_id=client.id).filter_by(flight_id = Flight.id)
    data = query.all()
    return render_template('mytickets.html',flights=data)


@mod.route('/deleteticket', methods=['POST'])
def deleteticket():
    id = request.form['id']
    ticket = Ticket.query.filter_by(id=id).one()
    flight=Flight.query.filter_by(id=ticket.flight_id).one()
    flight.numberseats = flight.numberseats + 1
    Flight.query.filter_by(id=flight.id).update({"numberseats": flight.numberseats})
    Ticket.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/mytickets')


