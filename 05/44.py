# -*- coding: utf-8 -*-
from Chunk_41 import Chunk
from Chunk_41 import read_cabocha, parse_cabocha
import pydot
from subprocess import Popen, PIPE
import codecs

def visualize(cabocha):
    sentences = read_cabocha(cabocha)
    g = pydot.Dot()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.morphs:
                e_dst = chunk.surface()
            for src in chunk.srcs:
                if sentence[src].morphs:
                    e_src = sentence[src].surface()
                    g.add_edge(pydot.Edge(e_src, e_dst))
    
    g.write_jpeg(cabocha + '.jpg')

def visualize_from_text(text, name):
    tmp = codecs.open(name + '.txt', 'w', 'utf-8')
    tmp.write(text)
    tmp.close()
    p = Popen("cabocha -f1 < " + name + ".txt > " + name + ".txt.cabocha", shell=True)
    p.wait()
    sentences = read_cabocha(name + '.txt.cabocha')
    Popen("rm " + name + ".*", shell=True)
    g = pydot.Dot()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.morphs:
                e_dst = chunk.surface()
            for src in chunk.srcs:
                if sentence[src].morphs:
                    e_src = sentence[src].surface()
                    print e_src + u'->' + e_dst
                    g.add_edge(pydot.Edge(e_src, e_dst))
    g.write_jpg(name + '.jpg')
    
