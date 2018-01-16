from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import wsgi

from index import *

from scoreText import *

import json

app = Flask(__name__)

emojiList = {
    0: u'\U0001F602',
    1: u'\U0001F612',
    2: u'\U0001F629',
    3: u'\U0001F62D',
    4: u'\U0001F60D',
    5: u'\U0001F614',
    6: u'\U0001F44C',
    7: u'\U0001F60A',
    8: u'\U0001f604',
    9: u'\U0001f604',
    10: u'\U0001f604',
    11: u'\U0001f604',
    12: u'\U0001f604',
    13: u'\U0001f604',
    14: u'\U0001f604',
}

@app.route("/<strings>")
def main(strings):
    
    result = score(strings)
    top1 = result[0]['top5'][0]

    return str(top1)

@app.route("/x/<strings>")
def hello(strings):
    event = {
        'input': strings
    }
    context = object()
    result = handler(event, context)

    return json.dumps(result, ensure_ascii=False)

SERVER = wsgi.WSGIServer(('127.0.0.1', 5000), app)
SERVER = wsgi.WSGIServer(('0.0.0.0', 5000), app)
SERVER.serve_forever()