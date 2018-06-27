# -*- coding: utf-8 -*-
import sys

n = 0

for (i, val) in enumerate(sys.argv):
    if val[0] == '-':
        n = int(sys.argv[i + 1])
filename = sys.argv[-1]

f = open(filename)
lines = f.read().split('\n')
f.close()

lines = filter(lambda str: str != '', lines)
for line in lines[-n:]:
    print(line)
