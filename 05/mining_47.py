# -*- coding: utf-8 -*-
from Chunk_41 import read_cabocha
import codecs

def verb_mining():
    text = read_cabocha('neko.txt.cabocha')
    fout = codecs.open('mining.txt', 'w', 'utf-8')
    for sentence in text:
        for chunk in sentence:
            verb = chunk.first_verb()
            if verb:
                is_sahen = False
                is_wo = False
                sahen = None
                for src in chunk.srcs:
                    is_sahen = False
                    is_wo = False
                    sahen = None
                    for morph in sentence[src].morphs:
                        if morph.pos1 == u'サ変接続':
                            is_sahen = True
                            sahen = src
                        if morph.surface == u'を':
                            is_wo = True
                if is_sahen and is_wo:
                    line = sentence[src].surface() + verb + '\t'
                    cases = []
                    surfaces = []
                    for src in chunk.srcs:
                        case = sentence[src].case()
                        if case:
                            cases.append(case)
                            surfaces.append(sentence[src].surface())
                    if cases:
                        line = line + u' '.join(sorted(cases)) + '\t' + u' '.join(sorted(surfaces))
                        fout.write(line + '\n')
    fout.close()
