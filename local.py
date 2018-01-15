from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import wsgi

from index import *

import json

app = Flask(__name__)

@app.route("/<strings>")
def hello(strings):
    event = {
        'input': strings
    }
    context = object()
    result = handler(event, context)
    return json.dumps(result)

SERVER = wsgi.WSGIServer(('127.0.0.1', 5000), app)
SERVER = wsgi.WSGIServer(('0.0.0.0', 5000), app)
SERVER.serve_forever()