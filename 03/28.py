# -*- coding: utf-8 -*-
import re
import extract_template as ext

template = ext.extract_template()
emph_mark = ur'(\'{1,3})([^\']+)\1'
int_mark = ur'\[\[([^[\]#|]+)(#[^[\]|]+)*(\|[^[\]#|]+)*\]\]'
lang_mark = ur'\{\{lang\|[^}|]+\|([^}|]+)\}\}'

for k, v in template.items():
    # enphasize markup
    match = re.search(emph_mark, v)
    if match:
        template[k] = (match.groups())[1]
    # internal link markup
    match = re.search(int_mark, v)
    if match:
        #print(match.group())
        #print(match.groups())
        if (match.groups())[2]:
            template[k] = (match.groups())[2][1:]
        else:
            template[k] = (match.groups())[0]
    # template markup
    match = re.search(lang_mark, v)
    if match:
        template[k] = (match.groups())[0]

for k, v in template.items():
    print(k + '=' + v)
