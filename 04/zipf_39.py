# -*- coding: utf-8 -*-
from read_mecab_30 import *
import codecs

words = readmecab()
freq = {}

for word in words:
    if word['base'] in freq:
        freq[word['base']] = freq[word['base']] + 1
    else:
        freq[word['base']] = 1

freq = sorted(freq.items(), key = lambda x: -x[1])

output = codecs.open('zipf.dat', 'w', 'utf-8')
for (i, (w, f)) in enumerate(freq):
    output.write(str(i + 1) + u'\t' + str(f) + u'\n')
output.close()


# $ gnuplot
# $ plot "zipf.dat" using 1:2 with line
