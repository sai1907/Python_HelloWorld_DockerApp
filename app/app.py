# -*- coding: UTF-8 -*-
"""
hello_flask: Python-Flask webapp
"""
from flask import Flask, jsonify, request, render_template   # From module flask import class Flask
import datetime

app = Flask(__name__)    # Construct an instance of Flask class for our webapp

app.config["DEBUG"] = True
status = {"uptime": "up since " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/healthz', methods=['GET'])
def healthz():
    status_version = {"status": "200 OK", "version": "0.0.1"}
    status.update(status_version)
    return jsonify(status)

if __name__ == '__main__':  # Script executed directly
    app.run('0.0.0.0', port=8080)
