"""Monitoring example"""

from datetime import datetime
from functools import wraps
from time import monotonic
import socket
import sqlite3

from flask import Flask, jsonify
from influxdb import InfluxDBClient

app = Flask(__name__)

_conn = None
_influx = InfluxDBClient(database='udp', use_udp=True, udp_port=8089)

earnings_sql = '''
SELECT
    DATE(pickup) AS day,
    vendor,
    SUM(total) AS earnings
FROM taxi
GROUP BY day, vendor
'''


def timed(fn):
    points = [{
            'measurement': '{}_duration'.format(fn.__name__),
            'tags': {
                'host': socket.gethostname(),
            },
            'time': None,  # Filled by wrapper
            'fields': {
                'value': None,  # Filled by wrapper
            },
        }]

    @wraps(fn)
    def wrapper(*args, **kw):
        start = monotonic()
        try:
            return fn(*args, **kw)
        finally:
            points[0]['fields']['value'] = monotonic() - start
            time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
            points[0]['time'] = time
            _influx.write_points(points)

    return wrapper


def get_cursor():
    global _conn

    if _conn is None:
        _conn = sqlite3.connect(
            'taxi.db', detect_types=sqlite3.PARSE_DECLTYPES)

    return _conn.cursor()


@app.route('/earnings')
@timed
def earnings():
    cur = get_cursor()
    cur.execute(earnings_sql)

    rows = [list(row) for row in cur]

    return jsonify(
        columns=[col[0] for col in cur.description],
        rows=rows,
        count=len(rows),
    )


if __name__ == '__main__':
    app.run(port=8080)
