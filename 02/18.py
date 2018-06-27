import sys

f = open(sys.argv[-1])
lines = f.read().split('\n')
f.close()

lines = filter(lambda str: str != '', lines)

for (i, elem) in enumerate(lines):
    lines[i] = elem.split('\t')

lines.sort(key = lambda x: x[2], reverse=True)

for line in lines:
    print('\t'.join(line))
