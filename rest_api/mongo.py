from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SEC_EDGAR'
app.config['MONGO_USERNAME'] = 'rmarathay'
app.config['MONGO_PASSWORD'] = '1234'
app.config['MONGO_AUTH_SOURCE'] = 'admin'
app.config['MONGO_AUTH_MECHANISM'] = 'SCRAM-SHA-1'
app.config['MONGO_URI'] = 'mongodb://45.55.48.43:27017/SEC_EDGAR'

mongo = PyMongo(app)


@app.route('/')
def hello():
	return 'Hello, World!'
