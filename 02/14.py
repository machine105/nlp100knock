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

for line in lines[0:n]:
    print(line)
    
