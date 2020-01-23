#!/bin/bash
# Run influxdb + chronograf docker

docker run \
    -p 8086:8086 \
    -p 8089:8089/udp \
    -v ${PWD}/influxdb.conf:/influxdb.conf \
    influxdb:1.4-alpine -config /influxdb.conf &

docker run --network=host chronograf:1.3-alpine
