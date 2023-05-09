#!/bin/sh

# turn on bash's job control
set -m
./manage.py crontab add &
./manage.py runserver 0.0.0.0:8000 &
crond -l 2 -f
#./manage.py migrate &

# now we bring the primary process back into the foreground and leave it there
fg %2
