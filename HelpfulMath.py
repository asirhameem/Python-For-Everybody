math = input()

list = math.split("+")

string = str
newList = []

for i in range(0,len(list)):
    n = int(list[i])
    newList.append(n)

newList.sort()

done = "+".join(map(str, newList))

print(done)
