# -*- coding: utf-8 -*-

import extract_template as exTemp
import urllib2
import urllib
import json

endpoint = 'https://ja.wikipedia.org/w/api.php'

template = exTemp.extract_template()

title = urllib.quote(template[u'国旗画像'])

request = endpoint + '?action=query&format=json&titles=File:' + title + '&prop=imageinfo&&iiprop=url'
print request

ret = urllib2.urlopen(request)
obj = json.loads(ret.read())
#print json.dumps(obj, indent=2, separators=(',', ':'))
print obj['query']['pages']['-1']['imageinfo'][0]['url']
