# -*- coding: utf-8 -*-
from read_mecab_30 import *

words = readmecab()
verbs = []

for word in words:
    if word['pos'] == u'名詞' and word['pos1'] == u'サ変接続':
        verbs.append(word['base'])

for verb in verbs:
    print verb
