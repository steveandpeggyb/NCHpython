#!/usr/bin/env python
# Call the user data HTTP API

import requests
import json

with open('cookies.json') as fp:
    cookies = json.load(fp)

url = 'http://localhost:8080/user/daffy'
resp = requests.get(url, cookies=cookies)
print(resp.json())
