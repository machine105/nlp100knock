#!/usr/sh

NUM=`wc -l $2 | sed -e 's/[^0-9]//g'`
R=`expr $NUM % $1`
R=`expr $1 \- $R`
R=`expr $R % $1`
NUM=`expr $NUM \+ $R`
NUM=`expr $NUM \/ $1`
split -l $NUM $2 $2-
