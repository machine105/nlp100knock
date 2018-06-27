# -*- coding: utf-8 -*-
import regex
import england as uk


def extract_template():
    text = uk.read_json_of_england()

    matches = regex.finditer(ur'(?<rec>\{\{(?:[^{}]+|(?&rec))*\}\})', text)

    template = {}

    for match in matches:
        str = match.group()
        if str[0:6] == u'{{基礎情報':
            #    print(str)
            attrs = regex.findall(ur'\|([^|]+) = ([^|].+)', str)
            for attr in attrs:
                template[attr[0]] = attr[1]

    #for k, v in template.items():
    #    print(k + '=' + v)

    return template

extract_template()
