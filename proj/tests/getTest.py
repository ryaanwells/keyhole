import json
import requests

headers = {'content-type': 'application/json'}
payload = {'locks': '/keyhole/resources/1/', 
           'allowed_methods': ['/keyhole/methods/1/']
}


r = requests.get('http://127.0.0.1:8000/keyhole/key/', data=json.dumps(payload), headers=headers, auth=('ryan', 'a'))

print r.text
