#!/usr/bin/env python
# Call the register HTTP API

import requests
import json

headers = {
    'Content-Type': 'application/json',
}
request = {
    'name': 'Daffy Duck',
}

url = 'http://localhost:8080/register/daffy'

resp = requests.post(url, headers=headers, data=json.dumps(request))
print(resp.json())

# Save cookies
with open('cookies.json', 'w') as out:
    json.dump(dict(resp.cookies), out)
