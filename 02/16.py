# -*- coding: utf-8 -*-
import sys

N = 0
for (i, val) in enumerate(sys.argv):
    if val[0] == '-':
        N = int(sys.argv[i + 1])
filename = sys.argv[-1]

f = open(filename)
lines = f.read().split('\n')
f.close()

l = (len(lines) - len(lines) % N + 1) / N
for i in range(N):
    f = open(filename + '-%d'%(i,), 'w')
    f.write('\n'.join(lines[i * l : (i + 1) * l]))

    
