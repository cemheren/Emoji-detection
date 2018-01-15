from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import wsgi

from index import *

import json

app = Flask(__name__)

@app.route("/")
def hello():
    event = object()
    context = object()
    result = handler(event, context)
    return json.dumps(result)

# @app.route("/cluster/<strings>")
# def cluster(strings):
#     names = strings.split(" ")
#     return json.dumps(result)

# @app.route("/name/<strings>")
# def name(strings):
#     names = strings.split(" ")
#     return json.dumps(result)

# @app.route("/tags/<strings>")
# def tags(strings):
#     names = strings.split(" ")
#     return json.dumps(result)

SERVER = wsgi.WSGIServer(('127.0.0.1', 5000), app)
# server = wsgi.WSGIServer(('0.0.0.0', 5000), app)
SERVER.serve_forever()