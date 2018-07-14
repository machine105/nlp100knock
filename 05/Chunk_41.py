# -*- coding: utf-8 -*-
from Morph_40 import Morph
import codecs
import re

class Chunk:
    def __init__(self, _morphs, _dst, _srcs = []):
        self.morphs = _morphs
        self.dst = _dst
        self.srcs = _srcs

    def __repr__(self):
        ret = u''
        ret = ret + u'->' + str(self.dst) + u'\n<-'
        for src in self.srcs: 
            ret = ret  + str(src) + u','
        ret = ret + u'\n'
        for morph in self.morphs:
            ret = ret + morph.surface
        ret = ret + u'\n'
        return ret.encode('utf-8')

def read_cabocha():
    ret = [] # list of sentences
    fin = codecs.open('neko.txt.cabocha', 'r', 'utf-8')
    cont = fin.read().split('\n')
    fin.close()

    sentence = [] # list of Chunk
    chunk = None
    dst = {}
    for line in cont:
        chunk_mark = re.match(ur'\* ([0-9]+) (-?[0-9]+)D .*', line)
        if chunk_mark:
            if chunk:
                sentence.append(chunk)
            if chunk_mark.group(1) in dst:
                chunk = Chunk([], int(chunk_mark.group(2)), dst[chunk_mark.group(1)])
            else:
                chunk = Chunk([], int(chunk_mark.group(2)))
            if chunk_mark.group(2) in dst:
                dst[chunk_mark.group(2)].append(int(chunk_mark.group(1)))
            else:
                dst[chunk_mark.group(2)] = [int(chunk_mark.group(1))]
        morph_mark = re.match(ur'(.+)\t(.+),(.+),.+,.+,.+,.+,(.+),.+,.+', line)
        if morph_mark:
            chunk.morphs.append(Morph(morph_mark.group(1), morph_mark.group(4), morph_mark.group(2), morph_mark.group(3)))
        if line == 'EOS':
            sentence.append(chunk)
            ret.append(sentence)
            chunk = None
            sentence = []
            dst = {}
    return ret
