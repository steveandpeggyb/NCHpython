"""Number of jobs in database"""

from http import HTTPStatus

from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import DictCursor


app = Flask(__name__)
cursor = None


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
    count = get_num_jobs()
    return jsonify(count=count)


if __name__ == '__main__':
    cursor = db_connect()
    app.run(port=8080)
