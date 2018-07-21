# -*- coding: utf-8 -*-
import re

def split_sentence(text):
    sentences = []
    pattern = ur'[.;:?!]\s[A-Z]'
    match = re.search(pattern, text)
    while match:
        sentences.append(text[:match.start(0) + 1])
        text = text[match.end(0) - 1:]
        match = re.search(pattern, text)
    return sentences

fin = open('nlp.txt', 'r')
text = fin.read()
fin.close()
fout = open('sentences.txt', 'w')
for sentence in split_sentence(text):
    fout.write(sentence + '\n')
fout.close()
    
