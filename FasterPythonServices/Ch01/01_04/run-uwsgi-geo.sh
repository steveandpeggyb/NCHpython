#!/bin/bash

uwsgi \
    --http :8080 \
    --wsgi-file geo_httpd.py \
    --callable app \
    --master \
    --logto geo_httpd.log \
    --processes 8
