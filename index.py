import datetime
import simplejson as sjson

from scoreText import *

def handler(event, context):
    
    try:
        result = score(u'Score me like one of your French girls.')
    except Exception, e:
        result = e
    
    print result

    data = {
        'output': result,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': sjson.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
