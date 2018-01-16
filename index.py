try:
    import unzip_requirements
except ImportError:
    pass

import datetime
import json

from scoreText import *

def handler(event, context):
    
    try:
        result = score(event['input'])
    except Exception, e:
        result = e
    
    print result

    data = {
        'output': result,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data, ensure_ascii=False),
            'headers': {'Content-Type': 'application/json'}}
