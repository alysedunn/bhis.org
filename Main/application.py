from flask import Flask, render_template
from ses_mailer import Mail

application = Flask(__name__)

mail = Mail(aws_access_key_id="",
            aws_secret_access_key="",
            region="us-east-1d",
            sender="website@contactform.com",
            reply_to="alyse.dunn@gmail.com",
            template="/contact")
mail.init_app(application)

@application.route('/')
def homepage ():
    return render_template('index.html')

@application.route('/aboutus', methods=['GET', 'POST'])
def aboutus ():
    return render_template('aboutus.html')

@application.route('/questions', methods=['GET', 'POST'])
def questions ():
    return render_template('questions.html')

@application.route('/forms', methods=['GET', 'POST'])
def forms ():
    return render_template('forms.html')

@application.route('/pricing', methods=['GET', 'POST'])
def pricing ():
    return render_template('pricing.html')

@application.route('/contact', methods=['GET', 'POST'])
def contact ():
    mail.send(to="alyse.dunn@gmail.com",
            #   source="website@contactform.com",
              subject="BHIS test subject",
              body="BHIS test body")
    return render_template('contact.html')

if __name__ == "__main__":
    application.debug = False
    application.run()
