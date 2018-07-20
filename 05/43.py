# -*- coding: utf-8 -*-
from Chunk_41 import Chunk
from Chunk_41 import read_cabocha
import codecs

# noun -> verb
def relations_nv():
    fout = codecs.open('out43.txt', 'w', 'utf-8')
    text = read_cabocha('neko.txt.cabocha')
    for sentence in text:
        for chunk in sentence:
            if chunk.has_verb():
                line = chunk.surface()
                tmp = u''
                for src in chunk.srcs:
                    if sentence[src].morphs and sentence[src].has_noun():
                        tmp = tmp + u'\t' + sentence[src].surface()
                if tmp:
                    line = line + tmp + '\n'
                    fout.write(line)
    fout.close()
            
            
