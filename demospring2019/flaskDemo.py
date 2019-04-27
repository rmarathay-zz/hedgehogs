from flask import Flask, url_for, session, redirect, escape, request, render_template
from secretParser import getSecret
from LoginForm import RegistrationForm
from flask_login import LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy
import os.path
from werkzeug.urls import url_parse
from DataProcessingDriver import MainWrapper
from User import User

db = SQLAlchemy()
app = Flask(__name__)
db.init_app(app)
app.secret_key = getSecret()[0]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rcos:' + getSecret()[1] + '@206.189.181.163/rcos' 
login = LoginManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@login.user_loader
def load_user(id):
    return User.query.get(id)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if (request.method == 'POST'):
		email = request.form.get('email')
		name = request.form.get('name')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()
		if user is not None:
			return redirect(url_for('register'))
		user = User(username=name, email=email, password_hash=password)
		db.session.add(user)
		db.session.commit()
		flash('New User Created!')
		return redirect(url_for('login'))


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

@app.route('/login', methods=['GET', 'POST'])
def login():
	if (request.method == 'POST'):
		email = request.form.get('email')
		name = request.form.get('name')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()
		if user is None:
			flash('User not found!')
			return redirect(url_for(login))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
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