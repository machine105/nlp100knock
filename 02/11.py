# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1])
str = f.read()
f.close()

str = str.replace('\t', ' ')

print(str)
