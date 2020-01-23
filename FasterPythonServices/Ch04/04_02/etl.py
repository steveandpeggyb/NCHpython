"""Load logs to database ETL - example on using threads"""
from datetime import datetime, timezone
from http import HTTPStatus
from time import monotonic
import logging
import re

from flask import Flask, request, abort, jsonify
from psycopg2.pool import ThreadedConnectionPool

app = Flask(__name__)
pool = None  # Connection pool


# uplherc.upl.com - - [01/Aug/1995:00:00:07 -0400] "GET /sched HTTP/1.0" 304 0
regexp = r'^([^ ]+) - - \[([^\]]+)\] "([A-Z]+) ([^ ]+)[^"]*" (\d+) (\d+|-)'

schema_sql = '''
CREATE TABLE logs (
    file TEXT,
    line INTEGER,
    client TEXT,
    time TIMESTAMP,
    method TEXT,
    path TEXT,
    status INTEGER,
    size INTEGER
);
'''

insert_sql = '''
INSERT INTO logs
    (file, line, client, time, method, path, status, size)
    VALUES
    (
        %(file)s, %(line)s, %(client)s, %(time)s, %(method)s, %(path)s,
        %(status)s, %(size)s
    );
'''


def parse_time(timestr):
    """Parse time string to datetime, return UTC time"""
    dt = datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z')
    # Convert to naive UTC time
    return dt.astimezone(timezone.utc).replace(tzinfo=None)


def parse_line(line):
    """Parse a log line"""
    match = re.search(regexp, line.decode('utf-8'))
    if not match:
        return

    client, time, method, path, status, size = match.groups()
    return {
        'client': client,
        'time': parse_time(time),
        'method': method,
        'path': path,
        'status': int(status),
        'size': 0 if size == '-' else int(size),
    }


def iter_batches(fp, file_name, batch_size=1000):
    """Iterate of file and return batches of logs"""
    batch = []
    for lnum, line in enumerate(fp, 1):
        data = parse_line(line)
        if not data:
            logging.error('%s:%s: cannot parse: %s', file_name, lnum, line)
            continue

        data.update({
            'file': file_name,
            'line': lnum,
        })

        batch.append(data)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


def insert(batch):
    conn = pool.getconn()
    try:
        cur = conn.cursor()
        cur.executemany(insert_sql, batch)
        conn.commit()
    finally:
        pool.putconn(conn)

    return len(batch)


@app.route('/etl', methods=['POST'])
def etl():
    log_file = request.files.get('log', None)
    if not log_file:
        abort(HTTPStatus.BAD_REQUEST)

    count = 0
    start = monotonic()

    conn = pool.getconn()
    try:
        cur = conn.cursor()
        for batch in iter_batches(log_file.stream, log_file.name):
            cur.executemany(insert_sql, batch)
            count += len(batch)
        conn.commit()
    finally:
        pool.putconn(conn)

    end = monotonic()

    return jsonify(
        count=count,
        time=end - start,
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    from sys import stderr

    parser = ArgumentParser(description='ETL HTTP server')
    parser.add_argument(
        '--init-db', help='initialize database', action='store_true',
        default=False)

    args = parser.parse_args()

    pool = ThreadedConnectionPool(0, 50, host='localhost', user='postgres')

    if args.init_db:
        conn = pool.getconn()
        cur = conn.cursor()
        cur.execute(schema_sql)
        conn.commit()
        raise SystemExit

    logging.basicConfig(
        stream=stderr,
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )

    app.run(port=8080)
