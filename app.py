from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://xxuser:welcome1@129.146.85.135/sampledb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://xxuser:welcome1@127.0.0.1/sampledb'
#app.secret_key = "flask rocks!"

#db = SQLAlchemy(app)