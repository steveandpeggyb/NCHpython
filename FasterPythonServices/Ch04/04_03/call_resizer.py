#!/usr/bin/env python
"""Calling resizer web API"""

import requests
from argparse import ArgumentParser, FileType

parser = ArgumentParser(description='client for resize web API')
parser.add_argument('image', help='image file', type=FileType('rb'))
parser.add_argument(
    '--output', help='output file', type=FileType('wb'), default='-')
parser.add_argument(
    '--ratio', help='scale ratio (e.g. 0.7)', default=0.5, type=float)
parser.add_argument(
    '--api-url', help='API URL', default='http://localhost:8080/resize')

args = parser.parse_args()

headers = {
    'Content-Type': 'application/octet-stream',
}

params = {
    'ratio': str(args.ratio),
}

data = args.image.read()

resp = requests.post(args.api_url, data=data, headers=headers, params=params)
args.output.write(resp.content)
