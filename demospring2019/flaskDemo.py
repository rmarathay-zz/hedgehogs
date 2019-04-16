from flask import Flask, url_for, session, redirect, escape, request, render_template
from secretParser import getSecret
from LoginForm import RegistrationForm
from flask_login import LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy
from DataProcessingDriver import mainMethod
from graphMatPlotLib import gen_graph

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = getSecret()[0]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rcos:' + getSecret()[1] + '@206.189.181.163/rcos' 
login = LoginManager(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	return render_template('registration.html')

@app.route('/tools', methods=['GET', 'POST'])
def tools():
	temp = 0
	if (request.method == 'POST'):
		result = request.form['user_input']
		if (result!=''):
			mainMethod()
			# gen_graph(result)
			# temp = 'static/' + result + '.png'
			temp = 'static/close2.png'
	return render_template('tools.html', url = temp)

@app.route('/login')
def login():
	form = RegistrationForm(request.form)
	# if form.validate_on_submit():
		# return redirect('/success')
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))


@app.route('/data/<ticker>')
def getStock(ticker):
	return ticker + ' IS THE BEST COMPANY!'

@app.route('/credits')
def credits():
	return 'Icon made by Freepik from www.flaticon.com'