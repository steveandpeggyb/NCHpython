from os.path import abspath, dirname
import sqlite3

from flask import Flask, request
from pybloom_live import BloomFilter

here = dirname(abspath(__file__))

db_file = '{}/events.db'.format(here)
app = Flask(__name__)
id_cache = BloomFilter(1000000)
cursor = None


def db_connect():
    schema = '''
    CREATE TABLE IF NOT EXISTS events (
        id CHAR(32) PRIMARY KEY
    );
    '''
    conn = sqlite3.connect(db_file)
    conn.executescript(schema)
    return conn.cursor()


def event_in_db(event_id):
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    return cursor.fetchone() is not None


def insert_new_event(event_id):
    cursor.execute('INSERT INTO events VALUES (?)', (event_id,))
    cursor.connection.commit()


def is_new(event_id):
    if event_id not in id_cache:
        return True

    return not event_in_db(event_id)


@app.route('/event/<event_id>', methods=['POST'])
def handle(event_id):
    if not is_new(event_id):
        return 'DUPLICATE'

    insert_new_event(event_id)
    id_cache.add(event_id)

    # Handle event
    return request.json['name']


if __name__ == '__main__':
    # Initial fill of cache
    cursor = db_connect()
    for event_id, in cursor.execute('SELECT id FROM events'):
        id_cache.add(event_id)

    app.run(port=8080)
