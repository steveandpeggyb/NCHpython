#!/bin/bash
# Run gunicorn with our hw.py application via Unix domain socket

case $1 in
    -h | --help ) echo "usage: $(basename 0)"; exit;;
esac

gunicorn \
	--bind  unix:/tmp/gunicorn.sock \
	--workers 16 \
	static:app
