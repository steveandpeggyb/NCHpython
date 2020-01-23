#!/bin/bash
# Run Redis server via docker

case $1 in
    -h | --help ) echo "usage: $(basename 0)"; exit;;
esac

docker run \
    -d \
    -p 6379:6379 \
    redis:alpine
