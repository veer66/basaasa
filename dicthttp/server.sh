#!/bin/sh
err=3
while test "$err" -eq 3 ; do
    python server.py
    err="$?"
done
