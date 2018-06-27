# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1])
lines = f.readlines()
f.close()

print(len(lines))
