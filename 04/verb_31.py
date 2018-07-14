# -*- coding: utf-8 -*-

from read_mecab_30 import *

words = readmecab()
verbs = []

for word in words:
    if word['pos'] == u'動詞':
        verbs.append(word['surface'])

for verb in verbs:
    print verb
