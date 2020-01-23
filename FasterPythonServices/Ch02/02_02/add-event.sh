#!/bin/bash
# Add event using the web API

curl \
	-X POST \
	-H 'Content-Type: application/json' \
	-d '{"name": "bugs"}' \
	http://localhost:8080/event/353
