# -*- coding: utf-8 -*-
import re

def split_word(sentence):
    ret =[re.sub(r'[^a-zA-Z]+', '', w) for w in sentence.split(' ')]
    return ret

fin = open('sentences.txt')
sentences = fin.read().split('\n')
fin.close()

fout = open('words.txt', 'w')
for words in map(lambda s: split_word(s), sentences):
    for word in words:
        
        if word:
            fout.write(word + '\n')
fout.close()
