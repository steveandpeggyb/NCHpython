"""Example of using cookies to avoid state in the server"""
from flask import Flask, request, abort, Response

from base64 import b64decode, b64encode
from datetime import datetime
from http import HTTPStatus
import json


app = Flask(__name__)

cookie_name = 'days'


def make_response(reply, cookie):
    """Create a JSON reponse with a cookie"""
    resp = Response(json.dumps(reply), mimetype='application/json')
    resp.set_cookie('days', cookie)
    return resp


@app.route('/user/<login>', methods=['GET'])
def user(login):
    """Login API"""
    cookie = request.cookies.get(cookie_name)
    if not cookie:
        abort(HTTPStatus.NOT_FOUND)

    data = json.loads(b64decode(cookie))
    if data['login'] != login:
        abort(HTTPStatus.UNAUTHORIZED)

    signed = datetime.fromtimestamp(data['signed'])
    duration = (datetime.now() - signed).total_seconds()

    reply = {
        'name': data['name'],
        'duration': duration,
    }

    return make_response(reply, cookie)


@app.route('/register/<login>', methods=['POST'])
def register(login):
    """Register API"""
    # In reality - check that it's a new user (use a database...)
    data = {
        'login': login,
        'signed': datetime.now().timestamp(),
        'name': request.json['name'],
    }

    cookie = b64encode(json.dumps(data).encode('utf-8'))
    return make_response({'ok': True}, cookie)


if __name__ == '__main__':
    app.run(port=8080)
