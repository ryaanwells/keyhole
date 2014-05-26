import json
import requests

headers = {'content-type': 'application/json'}
payload = {'user': '/keyhole/user/2/', 
           'locks': '/keyhole/resources/1/', 
           'allowed_methods': ['/keyhole/methods/1/']
}


r = requests.post('http://127.0.0.1:8000/keyhole/key/', data=json.dumps(payload), headers=headers)

print r.json()
