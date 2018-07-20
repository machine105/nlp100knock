# -*- coding: utf-8 -*-
from Chunk_41 import read_cabocha, Chunk
from Morph_40 import Morph
import codecs

def noun_to_noun_path():
    text = read_cabocha('neko.txt.cabocha')
    fout = codecs.open('n2n.txt', 'w', 'utf-8')
    for sentence in text:
        for i, chunk1 in enumerate(list(sentence)):
            for j, chunk2 in enumerate(list(sentence[i + 1:]), i + 1):
                if chunk1.has_noun() and chunk2.has_noun():
                    start_chunk = Chunk([], chunk1.dst, chunk1.srcs)
                    end_chunk = Chunk([], chunk2.dst, chunk2.srcs)
                    for morph in chunk1.morphs:
                        if morph.pos == u'名詞':
                            if not u'X' in map(lambda m: m.surface, start_chunk.morphs):
                                start_chunk.morphs.append(Morph(u'X', u'X', u'名詞', u''))
                        else:
                            start_chunk.morphs.append(morph)
                    for morph in chunk2.morphs:
                        if morph.pos == u'名詞':
                            if not 'Y' in map(lambda m: m.surface, end_chunk.morphs):
                                end_chunk.morphs.append(Morph(u'Y', u'Y', u'名詞', u''))
                        else:
                            end_chunk.morphs.append(morph)    
                    path = [start_chunk]
                    while path[-1].dst != -1 and path[-1] != chunk2:
                        path.append(sentence[path[-1].dst])
                    if path[-1] == chunk2:
                        # path i->j found
                        path = path[:-1]
                        line = u' -> '.join(map(lambda chunk: chunk.surface(), path))
                        line = line + ' -> Y' 
                        fout.write(line + u'\n')
                    else:
                        # path i->j not found, path represents the path i->root
                        # find k, where path i->root and j->root intersects
                        pathj = [end_chunk] # path j->root
                        while not pathj[-1].dst in map(lambda c: c.dst, path):
                            pathj.append(sentence[pathj[-1].dst])
                        k = pathj[-1].dst
                        k_in_path = 0
                        for pos, chunk in enumerate(path):
                            if chunk.dst == pathj[-1].dst:
                                k_in_path = pos + 1
                        line = ' -> '.join(map(lambda c: c.surface(), path[:k_in_path])) + ' | ' + ' -> '.join(map(lambda c: c.surface(), pathj)) + ' | ' + sentence[k].surface()
                        fout.write(line + u'\n')
    fout.close()
