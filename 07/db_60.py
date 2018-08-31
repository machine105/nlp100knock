# -*- coding: utf-8 -*-

import gzip
import json
from json.decoder import WHITESPACE
import plyvel
import sys

def loads_iter(s):
    size = len(s)
    decoder = json.JSONDecoder()

    end = 0
    while True:
        idx = WHITESPACE.match(s[end:]).end()
        i = end + idx
        if i >= size:
            break
        ob, end = decoder.raw_decode(s, i)
        progressbar(i, size, header='reading JSON') 
        yield ob

def progressbar(index, length, nchar=30, header=''):
    bar = ''
    for i in range(nchar):
        if i * length < nchar * index:
            bar = bar + '#'
        else:
            bar = bar + ' '
    bar = '......' + header + '[' + bar + '] %1f%% \r'%(float(100 * index) / length, )
    print bar,
    
def const_database(gzfile):
    with gzip.open(gzfile, 'rb') as f:
        db = plyvel.DB('kvs.ldb', create_if_missing=True)
        artists = list(loads_iter(f.read()))
        for index, artist in enumerate(artists):
            progressbar(index, len(artists), header='constructing DB')
            db.put(artist['name'].encode('utf-8'), artist.get(u'area', u'NOVALUE').encode('utf-8'))
        db.close()

if __name__ == '__main__':
    const_database('artist.json.gz')
