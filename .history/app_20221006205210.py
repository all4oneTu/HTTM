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
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path("project-id", mobnum)
    text_input = dialogflow.types.TextInput(text=message, language_code='en-US')
    query_input  = dialogflow

if __name__ == '__main__' : 
    app.run()