# -*- coding: utf-8 -*-
from read_mecab_30 import *
import codecs

words = readmecab()
freq = {}
max_freq = 0

for word in words:
    if word['base'] in freq:
        freq[word['base']] = freq[word['base']] + 1
    else:
        freq[word['base']] = 1
    if max_freq < freq[word['base']]:
        max_freq = freq[word['base']]

hist = [0] * (max_freq + 1)
for w, f in freq.items():
    hist[f] = hist[f] + 1

output = codecs.open('hist.dat', 'w', 'utf-8')
for i, data in enumerate(hist):
    output.write(str(i) + u'\t' + str(data) + u'\n')
output.close()


# $ gnuplot
# $ plot "hist.dat" using 1:2 with boxes notitle
