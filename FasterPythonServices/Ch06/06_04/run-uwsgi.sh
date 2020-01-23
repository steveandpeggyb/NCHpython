#!/bin/bash
# Run uwsgi with our application

uwsgi \
    --http :8081 \
    --wsgi-file user_data.py \
    --callable app \
    --master \
    --processes 16
