#! /bin/sh

export LANG=C
export TZ=JST-9

cd /usr/local/Gunicorn

gunicorn --config /usr/local/Gunicorn/settings.py myapp:app

