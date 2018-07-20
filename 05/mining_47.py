# -*- coding: utf-8 -*-
from Chunk_41 import read_cabocha
import codecs

def verb_mining():
    text = read_cabocha('neko.txt.cabocha')
    fout = codecs.open('mining.txt', 'w', 'utf-8')
    for sentence in text:
        # if を is in chunk, wo_pos represents the index of the char
        for wo_pos, chunk in enumerate(sentence):
            for morph in chunk.morphs:
                if morph.pos1 == u'サ変接続' and chunk.case() == u'を':
                    verb = sentence[chunk.dst].first_verb()
                    if verb:
                        # sentence[chunk.dst] must has verb
                        line = chunk.surface() + verb + u'\t'
                        cases = []
                        surfaces = []
                        for src in (chunk.srcs + sentence[chunk.dst].srcs):
                            if src == wo_pos:
                                continue
                            case = sentence[src].case()
                            if case:
                                cases.append(case)
                                surfaces.append(sentence[src].surface())
                        if cases:
                            line = line + u' '.join(sorted(cases)) + u'\t' + u' '.join(sorted(surfaces , key = lambda surface: surface[-1]))
                            fout.write(line + u'\n')
    fout.close()
