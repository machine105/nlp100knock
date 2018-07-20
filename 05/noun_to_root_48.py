# -*- coding: utf-8 -*-
from Chunk_41 import read_cabocha
import codecs

def path_noun_to_root():
    text = read_cabocha('neko.txt.cabocha')
    paths = []
    for sentence in text:
        for chunk in sentence:
            path = []
            for morph in chunk.morphs:
                if morph.pos == u'名詞':
                    path.append(chunk)
            if path:
                while path[-1].dst != -1:
                    # print path[-1].surface()
                    path.append(sentence[path[-1].dst])
                if len(path) > 1:
                    paths.append(path)
    return paths

fout = codecs.open('path_n2r.txt', 'w', 'utf-8')
for path in path_noun_to_root():
    fout.write(u'->'.join(map(lambda x: x.surface(), path)) + u'\n')
fout.close()
