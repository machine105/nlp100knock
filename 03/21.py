import england
import re

text = england.read_json_of_england()
pCategory = re.findall(r"\[\[Category:.+\]\]", text)

for cat in pCategory:
    print(cat)
