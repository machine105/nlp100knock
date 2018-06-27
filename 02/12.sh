#!/usr/sh

if [ $# -ge 1 ]; then
    cut -f 1 $1
    cut -f 2 $1
fi
