from flask import Flask, url_for, session, redirect, escape, request, render_template
from secretParser import getSecret
from LoginForm import RegistrationForm
from flask_login import LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy
import os.path
from DataProcessingDriver import MainWrapper

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
		if ('user_input' in request.form and 'data_input' in request.form):
			result = request.form['user_input']
			data_input_result = request.form.get('data_input')
			temp = 'static/' + result + '_' + data_input_result + '.png'
			if not os.path.isfile(temp):
				MainWrapper(result, data_input_result)
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