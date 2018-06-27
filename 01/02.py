# -*- coding: utf-8 -*-

str1 = u"パトカー"
str2 = u"タクシー"

str = ""
for (i, c) in enumerate(str1):
    str = str + c + str2[i]

print(str)
