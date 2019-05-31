from flask import Blueprint, request, session, render_template, flash

from app import db
from model.client import Client

mod = Blueprint('registration', __name__)


@mod.route('/reg', methods=['GET', 'POST'])
def reg():
    session.pop('logged_in', None)
    if request.method == 'POST':
        _name = request.form['username']
        _password = request.form['password']
        data = Client.query.filter_by(username=_name).all()
        if data != []:
            flash('This username has already exist!')
            return render_template('registration.html')
        else:
            flash('Success')
            reg = Client(username=_name, password=_password)
            db.session.add(reg)
            db.session.commit()
            session['user_id'] = Client.query.filter_by(username=_name).first().id
            session['logged_in'] = True
            session['name'] = _name
            return render_template('hello.html')
    return render_template('registration.html')
