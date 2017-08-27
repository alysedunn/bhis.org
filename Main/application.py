from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def homepage ():
    return render_template('index.html')

@application.route('/pricing', methods=['GET', 'POST'])
def pricing ():
    return render_template('pricing.html')

@application.route('/forms', methods=['GET', 'POST'])
def forms ():
    return render_template('forms.html')

@application.route('/test', methods=['GET', 'POST'])
def test ():
    return render_template('test.html')

if __name__ == "__main__":
    application.debug = False
    application.run()
