# -*- coding: utf-8 -*-
import json

def read_json_of_england():
    f = open('jawiki-country.json', 'r')
    buf = f.readlines()
    f.close()

    wiki = {}
    for line in buf:
        linebuf = json.loads(line, 'utf-8')
        wiki[linebuf['title']] = linebuf['text']

    return wiki[u'イギリス']
