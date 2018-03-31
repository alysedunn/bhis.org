import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message

application = Flask(__name__)

application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
application.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True

mail = Mail(application)

msg = Message(
    'Hello', sender='BHIS', recipients=[application.config['MAIL_USERNAME']])
msg.body = "This is the email body"


@application.route('/')
def homepage():
    return render_template('index.html')


@application.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')


@application.route('/questions', methods=['GET'])
def questions():
    return render_template('questions.html')


@application.route('/forms', methods=['GET'])
def forms():
    return render_template('forms.html')


@application.route('/pricing', methods=['GET'])
def pricing():
    return render_template('pricing.html')


@application.route('/contact', methods=['GET', 'POST'])
def contact():
    # name = request.form['username']
    mail.send(msg)
    # print str(name)
    return render_template('contact.html')


if __name__ == "__main__":
    application.debug = True
    application.run()
