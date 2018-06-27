# -*- coding: utf-8 -*-
import re
import england as uk

text = uk.read_json_of_england()

matches = re.findall(r'(={2,})([^=]+)={2,}', text)

for match in matches:
    print(u'セクション名: %s; レベル; %d'%(match[1], len(match[0]) - 1))
