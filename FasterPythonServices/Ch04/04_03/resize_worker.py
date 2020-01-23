from PIL import Image
from celery import Celery


app = Celery(
    'images',
    broker='redis://localhost',
    backend='redis://localhost',
)


@app.task
def resize(filename, ratio):
    img = Image.open(filename)

    size = [int(ratio * v) for v in img.size]
    rimag = img.resize(size)

    outfile = '{}.out'.format(filename)
    with open(outfile, 'wb') as out:
        rimag.save(out, img.format)

    return (outfile, img.format)
