"""We server using the resize Celery serivce"""
from flask import Flask, request, abort, Response
import resize_worker as worker

from uuid import uuid4
from http import HTTPStatus
from os import remove

app = Flask(__name__)


@app.route('/resize', methods=['POST'])
def resize():
    img_file = '/tmp/{}'.format(uuid4())
    with open(img_file, 'wb') as out:
        out.write(request.data)

    ratio = float(request.args.get('ratio', '0.5'))

    resp = worker.resize.delay(img_file, ratio)

    try:
        outfile, format = resp.get()
    except Exception as err:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    with open(outfile, 'rb') as fp:
        data = fp.read()

    remove(img_file)
    remove(outfile)

    return Response(data, mimetype='image/{}'.format(format.lower()))


if __name__ == '__main__':
    app.run(port=8080)
