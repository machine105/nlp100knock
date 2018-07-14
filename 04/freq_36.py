# -*- coding: utf-8 -*-
from read_mecab_30 import *

words = readmecab()
freq = {}

for word in words:
    if word['base'] in freq:
        freq[word['base']] = freq[word['base']] + 1
    else:
        freq[word['base']] = 1

freq = sorted(freq.items(), key = lambda x: -x[1])

for w, f in freq:
    print w + u': ' + str(f)
