from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/')
