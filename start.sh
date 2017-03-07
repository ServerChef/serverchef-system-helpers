#!/bin/bash
virtualenv ssh
source ssh/bin/activate
pip3 install -r requirements.txt
gunicorn main:app --bind unix:server.socket
