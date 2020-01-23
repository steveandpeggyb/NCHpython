#!/bin/bash
# Run nginx proxies to Python and serving static content

case $1 in
    -h | --help ) echo "usage: $(basename 0)"; exit;;
esac

docker run \
    --network host \
    -v ${PWD}/nginx.conf:/etc/nginx/nginx.conf:ro \
    -v /tmp/gunicorn.sock:/tmp/gunicorn.sock \
    -v ${PWD}:/var/www/ \
    nginx:alpine
