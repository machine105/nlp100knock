import re

str = 'abcabcdef'
matches = re.search(ur'(abc)+', str)

print(matches.group())
print(matches.groups())
