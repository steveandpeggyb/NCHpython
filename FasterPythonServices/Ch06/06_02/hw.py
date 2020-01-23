"""Flask example"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hi():
    return 'Hello\n'


if __name__ == '__main__':
    app.run(port=8080)
