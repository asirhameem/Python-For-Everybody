num = int(input())
n = 0
line = ""
while n<num:
    w = input()
    line = line + w
    n = n+1

list = sorted(line)
print(" ".join(list))
