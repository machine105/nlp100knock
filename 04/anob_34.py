# -*- coding: utf-8 -*-

from read_mecab_30 import *

words = readmecab()
nouns = []

for i, word in enumerate(words):
    if word['pos'] == u'名詞' and words[i + 1]['base'] == u'の' and words[i + 2]['pos'] == u'名詞':
        nouns.append(word['surface'] + u'の' + words[i + 2]['surface'])

for noun in nouns:
    print noun
        
