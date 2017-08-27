from flask import Flask, render_template

application = Flask(__name__)

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
    return render_template('contact.html')

if __name__ == "__main__":
    application.debug = False
    application.run()
