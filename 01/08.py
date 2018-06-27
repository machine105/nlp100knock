import re

def cipher(str):
    ret = ""
    for char in str:
        if re.match("[a-z]", char):
            ret = ret + chr(219 - ord(char))
        else:
            ret = ret + char
    return ret

def inverse(str):
    ret = ""
    for char in str:
        if re.match("[a-z]", char):
            ret = ret + chr(219 - ord(char))
        else:
            ret = ret + char
    return ret

print(cipher("I love Inori Minase"))
print(inverse(cipher("I love Inori Minase")))
