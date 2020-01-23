#!/bin/bash
# Run nginx as proxy to gunicorn with with HTTP or unix domain socket

case $1 in
    -h | --help ) echo "usage: $(basename 0) http|tcp"; exit;;
    http ) type=http;;
    unix ) type=unix; sock_vol="-v /tmp/gunicorn.sock:/tmp/gunicorn.sock";;
    * ) 1>&2 echo "error: unknown mode - $1"; exit 1;;
esac

docker run \
    --network host \
    -v ${PWD}/nginx-${type}.conf:/etc/nginx/nginx.conf:ro \
    ${sock_vol} \
    nginx:alpine
