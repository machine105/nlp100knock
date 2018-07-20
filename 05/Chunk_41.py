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
        for src in self.srcs: 
            ret = ret  + str(src) + u','
        ret = ret + u' -> '
        for morph in self.morphs:
            ret = ret + morph.surface
        ret = ret + u' -> '
        ret = ret + str(self.dst) + '\n'
        return ret.encode('utf-8')

    def __str__(self):
        return self.__repr__()

    def surface(self):
        ret = u''
        for morph in self.morphs:
            ret = ret + morph.surface
        return ret

    def has_verb(self):
        for morph in self.morphs:
            if morph.pos == u'動詞':
                return True
        return False

    def has_noun(self):
        for morph in self.morphs:
            if morph.pos == u'名詞':
                return True
        return False

    def first_verb(self):
        for morph in self.morphs:
            if morph.pos == u'動詞':
                return morph.base
        return None

    def case(self):
        for morph in reversed(self.morphs):
            if morph.pos == u'助詞':
                return morph.base
        return None

    def noun(self):
        for morph in self.morphs:
            if morph.pos == u'名詞':
                return morph.base
        return None

    def clean(self):
        for morph in self.morphs:
            if morph.pos == u'記号':
                self.morphs.remove(morph)

def read_cabocha(filename):
    ret = [] # list of sentences
    fin = codecs.open(filename, 'r', 'utf-8')
    cont = fin.read().split('\n')
    fin.close()

    sentence = [] # list of Chunk
    chunk = None
    # dst-src map
    dst = {}
    for line in cont:
        # head of chunk
        chunk_mark = re.match(ur'\* ([0-9]+) (-?[0-9]+)D .*', line)
        if chunk_mark:
            if chunk:
                # append previous chunk
                sentence.append(chunk)
            if chunk_mark.group(1) in dst:
                # if reading chunk is source of some other chunk
                chunk = Chunk([], int(chunk_mark.group(2)), dst[chunk_mark.group(1)])
            else:
                # if current chunk is source of no other chunk
                chunk = Chunk([], int(chunk_mark.group(2)))
            # add current chunk's destination to dst-src map
            if chunk_mark.group(2) in dst:
                dst[chunk_mark.group(2)].append(int(chunk_mark.group(1)))
            else:
                dst[chunk_mark.group(2)] = [int(chunk_mark.group(1))]
        # morph finded
        morph_mark = re.match(ur'(.+)\t(.+),(.+),.+,.+,.+,.+,(.+),.+,.+', line)
        if morph_mark:
            chunk.morphs.append(Morph(morph_mark.group(1), morph_mark.group(4), morph_mark.group(2), morph_mark.group(3)))
        # end of sentence
        if line == 'EOS':
            # add last chunk of the sentence
            if chunk:
                sentence.append(chunk)
            # add sentence(list) to return value
            if sentence:
                ret.append(sentence)
            # initialize temporary valuables
            chunk = None
            sentence = []
            dst = {}
    for sent in ret:
        for chunk in sent:
            chunk.clean()
    return ret

