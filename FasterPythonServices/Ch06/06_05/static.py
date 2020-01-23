"""Example serving static content"""
from flask import Flask


app = Flask(__name__)


@app.route('/dynamic')
def dynamic():
    return 'dynamic content'


if __name__ == '__main__':
    app.run(port=8080)
