from urllib import response
from flask import Flask
from flask import request, jsonify
import os 
from google.cloud import dialogflow_v2beta1
import requests
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private.json"
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/getMessage', methods=['POST'])
def root():
    message = request.form.get('Body')
    mobnum = request.form.get('From')
    session_client = dialogflow_v2beta1.SessionsClient()
    session = session_client.session_path("chatbot-xryq", mobnum)
    text_input = dialogflow_v2beta1.types.TextInput(text=message, language_code='en-US')
    query_input  = dialogflow_v2beta1.types.QueryInput(text=text_input)
 
    try : 
        response = session_client.detect_intent(session=s query_input=query_input)
    except InvalidArgument :
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    # sendMessage(mobnum, response.query_result.fulfillment_text)
    return jsonify({'fulfillmentText': response.query_result.fulfillment_text})

if __name__ == '__main__' : 
    app.run()