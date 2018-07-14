import re
import codecs

def readmecab():
    ret = []
    file = codecs.open('neko.txt.mecab', 'r', 'utf-8')
    cont = file.read()
    file.close()
    lines = cont.split('\n')

    for line in lines:
        buf = {}
        m = re.match(ur'(.+)\t(.+),(.+),.+,.+,.+,.+,(.+),.+,.+', line)
        if m:
            buf['surface'] = m.group(1)
            buf['base'] = m.group(4)
            buf['pos'] = m.group(2)
            buf['pos1'] = m.group(3)
            ret.append(buf)
    return ret
