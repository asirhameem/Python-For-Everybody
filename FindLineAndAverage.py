
fname = input("Enter file name: ")
fhandle = open(fname)
snum = 0
count = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    fnum = line[20:]
    num = float(fnum)
    snum = snum + num
    count = count+1
    #print(line)
    average = snum / count



print("Average spam confidence:", average)
