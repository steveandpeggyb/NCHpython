"""Service generating next ID"""
from flask import Flask, jsonify

from itertools import count

id_gen = count(1)

app = Flask(__name__)


@app.route('/next_id')
def next_id():
    """Next ID API"""
    return jsonify(id=next(id_gen))


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
