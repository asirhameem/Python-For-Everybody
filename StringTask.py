line = input()
length = len(line)
list = list(line.lower())

for i in range(0,length):
    for char in list:
        if char == "u" :
            list.remove(char)
        elif char == "a" :
            list.remove(char)
        elif char == "e" :
            list.remove(char)
        elif char == "i" :
            list.remove(char)
        elif char == "o" :
            list.remove(char)
        elif char == "y" :
            list.remove(char)



newlist = "." + ".".join(list)
print( newlist)
