#!/bin/bash
# Run PostgreSQL server via docker

case $1 in
    -h | --help ) echo "usage: $(basename 0)"; exit;;
esac

docker run \
    -d \
    --name postgres-aio \
    -p 5432:5432 \
    postgres:10-alpine
