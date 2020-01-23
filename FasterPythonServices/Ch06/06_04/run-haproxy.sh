#!/bin/bash
# Run HAProxy using docker

docker run \
    -v ${PWD}/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro \
    --network host \
    haproxy:alpine
