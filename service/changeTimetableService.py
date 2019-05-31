from flask import Blueprint, request, session, render_template, flash,redirect
from datetime import datetime
mod = Blueprint('changeTimetable', __name__)
from app import db
from model.flight import Flight
from model.airline import Airline




@mod.route('/createflight', methods=['GET', 'POST'])
def createflight():
    if request.method == 'POST':
        depart = datetime.strptime(request.form['depart'], "%d.%m.%Y %H:%M")
        arrive = datetime.strptime(request.form['arrive'], "%d.%m.%Y %H:%M")
        pointfrom = request.form['pointfrom']
        pointto = request.form['pointto']
        airline = request.form['airline']
        numberseats = request.form['numberseats']
        cost = request.form['cost']
        flight = Flight(depart=depart, arrive=arrive,pointfrom=pointfrom,pointto=pointto,airline=airline,numberseats=numberseats,cost=cost)
        db.session.add(flight)
        db.session.commit()
    air = Airline.query.all()
    return render_template('createflight.html',airlines = air)

@mod.route('/deleteflight', methods=['POST'])
def deleteflight():
    id = request.form['id']
    Flight.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/flight')