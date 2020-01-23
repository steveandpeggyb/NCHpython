"""Add a user using external API for user ID"""
from flask import Flask, jsonify
import requests

api_url = 'http://ec2-52-204-189-41.compute-1.amazonaws.com:8080/next_id'


app = Flask(__name__)


@app.route('/user/<login>', methods=['POST'])
def new_user(login):
    """New user API endpoint"""
    resp = requests.get(api_url)
    uid = resp.json()['id']

    return jsonify(ok=True, uid=uid, login=login)


if __name__ == '__main__':
    app.run(port=8080)
