import os

from flask import Flask, render_template, request
# from flask_mail import Mail, Message

application = Flask(__name__)

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
    return render_template('contact.html')


if __name__ == "__main__":
    application.debug = True
    application.run()
