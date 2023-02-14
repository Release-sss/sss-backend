#!/bin/bash

mng() {
    ./manage.py "$@"
}
shell() {
    mng shell
}
dev() {
    DJANGO_SETTINGS_MODULE=sss.$1.settings mng runserver
}
mg() {
    mng migrate $@
}
mmg() {
    mng makemigrations $@
}
smg() {
    mng showmigrations $@
}

if [ "$#" -eq "0" ]; then
    help
    exit 0
fi

trap exit SIGINT

eval "$@"
