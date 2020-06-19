x = input("Participants Number:")
par = int(x)
y = input("Going to next round:")
nex = int(y)

points = list()
sortedList = list()

for i in range(par):
    points.append(int(input("Enter point:")))

points.sort(reverse = True)

if all(v == 0 for v in points):
    print('0')
for zero in points:
    if zero == 0 and not points[0] == 0 :
        ind = points.index(zero)
        print(ind)
        break


val = points[nex]
chkNxt = nex
while chkNxt < par:
    nexx = points.get(val,0)
    chkNxt =chkNxt + 1
print(nex)
