year = input()
yr = int(year)
len = len(year)
print(len)

for i in range(yr,9000):
    count = 0
    for j in year:
        for k in year:
            if year[j] == year[k]:
                count = count + 1
                print(year[j])
    if(count == 4)
    print(i)
