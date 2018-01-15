import simplejson as sjson
import datetime

from scoreText import *

def handler(event, context):
    result = score(u'Score me like one of your French girls.')
    
    print result

    data = {
        'output': result,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': sjson.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
