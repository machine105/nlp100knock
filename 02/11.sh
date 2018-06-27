#!/usr/sh

if [ $# -ge 2 ]; then
    tr '\t' ' ' < $1 > $2
elif [ $# -ge 1 ]; then
    tr '\t' ' ' < $1
fi
