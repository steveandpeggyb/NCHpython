"""Example on using Redis for caching"""

from flask import Flask, jsonify
import sqlite3

conn = sqlite3.connect('black_ips.db')
app = Flask(__name__)


def is_black_ip(ip):
    """Check in database if IP is black"""
    cur = conn.cursor()
    cur.execute('SELECT COUNT(ip) FROM black_ips WHERE ip = ?', (ip,))

    row = cur.fetchone()
    return row[0] > 0


@app.route('/check_ip/<ip>')
def check_ip(ip):
    """ip for host API endpoint"""

    is_black = is_black_ip(ip)
    return jsonify(ip=ip, is_black=is_black)

@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run(port=8080)
