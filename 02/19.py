# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[-1])
lines = f.read().split('\n')
f.close()
lines = filter(lambda str: str != '', lines)

prefs = dict()
for line in lines:
    if (line.split('\t'))[0] in prefs:
        prefs[(line.split('\t'))[0]] += 1
    else:
        prefs[(line.split('\t'))[0]] = 1

for pref, n in sorted(prefs.items(), key = lambda x: -x[1]):
    print('%d:%s'%(n, pref,))

