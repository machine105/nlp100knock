# -*- coding: utf-8 -*-
import re
import england

text = england.read_json_of_england()

categories = re.findall(r'\[\[Category:(.+)\]\]', text)

for cate in categories:
    print(cate)
