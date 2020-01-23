#!/bin/bash
# Run gunicorn with our hw.py application either via HTTP or Unix domain socket

case $1 in
    -h | --help ) echo "usage: $(basename 0) http|tcp"; exit;;
    http ) bind=0.0.0.0:8081;;
    unix ) bind=unix:/tmp/gunicorn.sock;;
    * ) 1>&2 echo "error: unknown mode - $1"; exit 1;;
esac

gunicorn \
	--bind ${bind} \
	hw:app
