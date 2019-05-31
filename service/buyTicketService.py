from flask import Blueprint, request, render_template, redirect, flash, session

mod = Blueprint('buyService', __name__)
from app import db
from model.flight import Flight
from model.client import Client
from model.ticket import Ticket
from model.airline import Airline
from datetime import datetime


@mod.route('/flight', methods=['GET'])
def flight():
    data = Flight.query.all()
    return render_template('flight.html', flights=data)


@mod.route('/ticket', methods=['POST'])
def ticket():
    id = request.form['id']
    flight = Flight.query.filter_by(id=id).one()
    if flight.numberseats == 0:
        flash('Cannot buy')
    else:
        flight.numberseats = flight.numberseats - 1
        Flight.query.filter_by(id=id).update({"numberseats": flight.numberseats})
        client = Client.query.filter_by(username=session['name']).one()
        airline = Airline.query.filter_by(id=flight.airline).one()
        ticket = Ticket(client_id=client.id, flight_id=flight.id, cost=flight.cost)
        db.session.add(ticket)
        db.session.commit()
    return redirect('/flight')


@mod.route('/findflight', methods=['POST'])
def findflight():
    departtime =request.form["departtime"]
    pointto = request.form["pointto"]
    pointfrom = request.form["pointfrom"]
    query = Flight.query.filter(Flight.pointto.like("%" + pointto + "%")).filter(
        Flight.pointfrom.like("%" + pointfrom + "%"))
    if departtime!="":
        departtime = datetime.strptime( departtime, "%Y-%m-%d %H:%M")
        query = query.filter_by(depart=departtime)
    data = query.all()
    return render_template('flight.html', flights=data)
