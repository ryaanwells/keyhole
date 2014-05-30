import json
import requests

headers = {'HTTP_AUTHORIZATION': 'basic ryan:a'}

r = requests.get('http://127.0.0.1:8000/keyhole/user/', headers=headers, auth=('ryan', 'a'))

print r.json()
