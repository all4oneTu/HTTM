from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/')
def home():
    return "Hello World!"
@app.route('/api/getMessage', methods=['POST'])
def root()