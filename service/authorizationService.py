from flask import Blueprint, request, session, render_template, flash


mod = Blueprint('authorization', __name__)


from model.client import Client
from model.admin import Admin

@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _name = request.form['username']
        _password = request.form['password']
        data = Client.query.filter_by(username=_name).first()
        if data == None or not data.checkPas(_password):
            flash('Invalid username or password ')
        else:
            session['logged_in'] = True
            session['user_id'] = data.id
            session['name'] = _name
            session['admin'] = False
            flash('You were logged in')
            return render_template('hello.html')
    return render_template('login.html')


@mod.route('/loginadmin', methods=['GET', 'POST'])
def loginadmin():
    if request.method == 'POST':
        _name = request.form['username']
        _password = request.form['password']
        data = Admin.query.filter_by(username=_name).first()
        if data == None or not data.checkPas(_password):
            flash('Invalid username or password ')
        else:
            session['logged_in'] = True
            session['admin'] = True
            session['user_id'] = data.id
            session['name'] = _name
            flash('You were logged in')
            return render_template('hello.html')
    return render_template('adminlogin.html')


@mod.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return render_template('hello.html')
