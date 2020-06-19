import re

fname = "regex.txt"
fhandle = open(fname)
x = 0
list = list()
for line in fhandle:
    y = re.findall('[0-9]+',line)
    int(y)
    x = x + y
    if len(y) > 1:
        list.append(y)
print(x)
