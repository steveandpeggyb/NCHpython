"""Number of jobs in database"""

from http import HTTPStatus
from threading import Thread, Lock
from time import sleep

from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import DictCursor


app = Flask(__name__)
cursor = None
num_jobs_lock = Lock()
num_jobs = 0


def db_connect():
    """Connect to database, create jobs table if doesn't exists"""
    conn = psycopg2.connect(host='localhost', user='postgres')
    conn.cursor_factory = DictCursor

    schema = '''
    CREATE TABLE IF NOT EXISTS jobs (
        id CHAR(32) PRIMARY KEY,
        created TIMESTAMP DEFAULT NOW()
    );
    '''
    cur = conn.cursor()
    cur.execute(schema)
    conn.commit()
    return cur


def get_num_jobs():
    cursor.execute('SELECT COUNT(id) AS count FROM jobs')
    return cursor.fetchone()['count']


def num_jobs_thread():
    """Thread that update num_jobs global counter every second"""
    global num_jobs

    while True:
        value = get_num_jobs()
        with num_jobs_lock:
            num_jobs = value
        sleep(1)


@app.route('/job/<job_id>', methods=['POST'])
def add_job(job_id):
    """Add a job via API"""
    try:
        cursor.execute('INSERT INTO jobs (id) VALUES (%s)', (job_id,))
        cursor.connection.commit()
        return 'job #{} created\n'.format(job_id)
    except psycopg2.Error as err:
        cursor.connection.rollback()
        resp = jsonify(error=str(err))
        resp.status_code = HTTPStatus.BAD_REQUEST
        return resp


@app.route('/jobs/count')
def job_count():
    """Get current number of jobs"""
    with num_jobs_lock:
        count = num_jobs
    return jsonify(count=count)


if __name__ == '__main__':
    cursor = db_connect()
    num_jobs = get_num_jobs()
    Thread(target=num_jobs_thread, daemon=True).start()
    app.run(port=8080)
