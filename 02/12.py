# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1])
lines = f.readlines()
f.close()

out1 = []
out2 = []
for line in lines:
    cols = line.split('\t')
    out1.append(cols[0])
    out2.append(cols[1])
out1 = '\n'.join(out1)
out2 = '\n'.join(out2)
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
f1.write(out1)
f2.write(out2)
f1.close()
f2.close()
