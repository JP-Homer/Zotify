from re import L
from flask import Flask, jsonify
from flask_cors import CORS
from api import run
from api import happy
from api import sad
from api import angsty
from api import chill

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Everything works!'})

@app.route('/happy')
def happy_button():
    result = run()
    resxult = happy()

@app.route('/sad')
def sad_button():
    result = run()
    resxult = sad()

@app.route('/angsty')
def angsty_button():
    result = run()
    resxult = angsty()

@app.route('/chill')
def chill_button():
    result = run()
    resxult = chill()