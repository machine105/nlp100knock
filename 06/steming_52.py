# -*- coding: utf-8 -*-
from nltk.stem import PorterStemmer

ps = PorterStemmer()

fin = open('words.txt', 'r')
words = fin.read().split('\n')
fin.close()

fout = open('stems.txt', 'w')
for word, stem in [(w, ps.stem(w)) for w in words]:
    fout.write(word + '\t' + stem + '\n')
fout.close()
