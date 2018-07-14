# -*- coding: utf-8 -*-
import codecs
import re

class Morph:
    def __init__(self, _surface, _base, _pos, _pos1):
        self.surface = _surface
        self.base = _base
        self.pos = _pos
        self.pos1 = _pos1

def read_cabocha():
    ret = []
    fin = codecs.open('neko.txt.cabocha', 'r', 'utf-8')
    cont = fin.read()
    fin.close()
    cont = cont.split('\n')

    sentence = []
    for line in cont:
        morph = re.match(ur'(.+)\t(.+),(.+),.+,.+,.+,.+,(.+),.+,.+', line)
        if morph:
            sentence.append(Morph(morph.group(1), morph.group(4), morph.group(2), morph.group(3)))
        elif line == u'EOS':
            ret.append(sentence)
            sentence = []
    return ret
