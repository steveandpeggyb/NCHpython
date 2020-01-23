#!/bin/bash
# Run redis server using docker

docker run -d -p 6379:6379 redis:alpine
