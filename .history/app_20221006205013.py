from flask import Flask
from flask import request, jsonify
import os 
import dialogflow
import requests
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/getMessage', methods=['POST'])
def root():
    message = request.form.get('Body')
    mobnum = request.form.get('From')


if __name__ == '__main__' : 
    app.run()