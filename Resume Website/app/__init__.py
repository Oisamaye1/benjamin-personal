from flask import Flask, render_template, request
from flask_moment import Moment
from os import environ


app = Flask(__name__)
moment = Moment(app)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['E_PASSWORD'] = environ.get('EMAIL_PASSWORD')


from app import views
