userName =  input()

list = list(userName)

for i in list:
    for n in list:
        if list[i] == list[n] and i != n:
            count= count +1

print(count)
print(list)
