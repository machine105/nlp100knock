# -*- coding: utf-8 -*-
import re
import extract_template as ext

template = ext.extract_template()
emph_mark = ur'(\'{1,3})([^\']+)\1'

for k, v in template.items():
    match = re.search(emph_mark, v)
    if match:
        #print(match.group())
        #print((match.groups())[1])
        template[k] = (match.groups())[1]

for k, v in template.items():
    print(k + u'=' + v)
