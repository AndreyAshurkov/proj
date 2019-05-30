from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(DEBUG=True, SECRET_KEY='secretkey',
                  USERNAME='admin', PASSWORD='admin')
db = SQLAlchemy(app)


@app.route('/')
def main():
    #session.clear()
    return render_template('hello.html')


from service import registrationService
from service import authorizationService
from service import buyTicketService
from service import changeTimetableService
from service import changeTicketService

app.register_blueprint(changeTimetableService.mod)
app.register_blueprint(changeTicketService.mod)
app.register_blueprint(registrationService.mod)
app.register_blueprint(authorizationService.mod)
app.register_blueprint(buyTicketService.mod)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000, debug=True)
