
fname = input("Enter file name: ")
fhandle = open(fname)

line  = fhandle.read()

upline = line.upper().rstrip()
print(upline)
