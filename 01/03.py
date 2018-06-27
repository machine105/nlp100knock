import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

str = str.replace(",", " ")
str = str.replace(".", " ")
splited = str.split()

nums = []
for elem in splited:
    nums.append(len(elem))

print(nums)
