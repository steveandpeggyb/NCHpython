#!/bin/bash

case $1 in
    -h | --help ) echo "usage: $(basename 0)"; exit;;
esac

docker run \
    --network host \
    -v ${PWD}/nginx-unix.conf:/etc/nginx/nginx.conf:ro \
    -v /tmp/gunicorn.sock:/tmp/gunicorn.sock \
    nginx:alpine
