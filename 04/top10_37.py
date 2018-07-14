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

output = codecs.open('top10.dat', 'w', 'utf-8')
for w, f in freq[0:10]:
    output.write(w + u'\t' + str(f) + u'\n')
    print w + u': ' + str(f)
output.close()

# $ gnuplot
# $ plot "top10.dat" using 0:1:xtic(1) with boxes notitle
