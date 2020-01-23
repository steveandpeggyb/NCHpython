"""Compression example"""
from flask import Flask, Response, request
import gzip


app = Flask(__name__)
ctype = 'text/plain; charset=utf-8'

with open('sherlock-holmes.txt', 'rb') as fp:
    data = fp.read()

zdata = gzip.compress(data)


@app.route('/sherlock')
def sherlock():
    resp = Response(data, content_type=ctype)
    resp.headers['Connection'] = 'close'
    return resp


@app.route('/sherlockc')
def sherlockc():
    if 'gzip' not in request.headers.get('Accept-Encoding', ''):
        return data

    resp = Response(zdata, content_type=ctype)
    resp.headers['Content-Encoding'] = 'gzip'
    resp.headers['Connection'] = 'close'
    return resp


if __name__ == '__main__':
    app.run(port=8080)
