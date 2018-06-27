# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[-1])
lines = f.read().split('\n')
f.close()

lines = filter(lambda str: str != '', lines)

words = set()

for line in lines:
    cols = line.split('\t')
    words.add(cols[0])

for elem in words:
    print(elem)
