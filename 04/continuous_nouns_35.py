# -*- coding: utf-8 -*-
from read_mecab_30 import *

words = readmecab()
cont = []

itr = 0

while itr < len(words):
    if words[itr]['pos'] == u'名詞':
        pos = itr
        while words[itr]['pos'] == u'名詞':
            itr = itr + 1
        buf = u''
        if itr - pos > 1:
            for word in words[pos:itr]:
                buf = buf + word['surface'] #+ u'/'
            cont.append(buf)
    itr = itr + 1

for noun in cont:
    print noun
