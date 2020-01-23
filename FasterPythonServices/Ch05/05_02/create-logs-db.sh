#!/bin/bash
# Create logs database

# This script assume you running a postgresql docker container
#   docker run -d --name postgres -p5432:5432 postgres:10-alpine

# Exit on first error
set -e
# Echo commands
set -x

name=postgres-aio

docker cp nasa-logs-dump.tar.bz2 ${name}:/
docker exec ${name} bunzip2 /nasa-logs-dump.tar.bz2
docker exec ${name} psql -U postgres -c 'DROP TABLE IF EXISTS logs'
docker exec ${name} pg_restore -U postgres -F tar -C -d postgres nasa-logs-dump.tar
docker exec ${name} psql -U postgres -c 'SELECT COUNT(*) FROM logs'
