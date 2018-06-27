# -*- coding: utf-8 -*-
import re
import england as uk

text = uk.read_json_of_england()

matches = re.finditer(ur'(\[\[)?ファイル:([^|\]]+\|?)+\]\]|File:([^|\]]+\|?)+\]\]', text)

for match in matches:
    print(match.group())
