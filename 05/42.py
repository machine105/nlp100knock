# -*- coding: utf-8 -*-
from Chunk_41 import Chunk
from Chunk_41 import read_cabocha
import codecs

def relations():
    fout = codecs.open('out42.txt', 'w', 'utf-8')
    text = read_cabocha('neko.txt.cabocha')
    for sentence in text:
        for chunk in sentence:
            line = chunk.surface()
            for src in chunk.srcs:
                if sentence[src].morphs:
                    line = line + u'\t' + sentence[src].surface()
            line = line + '\n'
            fout.write(line)
    fout.close()
            
            
