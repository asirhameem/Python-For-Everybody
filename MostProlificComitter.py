fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
wordInLine = list()
wordList = list()
commonWord = dict()
bigWord = None
bigCount = None
for line in fhandle:
    line.rstrip()
    if line.startswith("From"):
        if not line.startswith("From:"):
            wordInLine = line.split()
            wordList.append(wordInLine[1])
for word in wordList :
    if word in wordList:
        commonWord[word] = commonWord.get(word,0)+1
for mail,mcount in commonWord.items() :
    if bigCount is None or mcount > bigCount:
        bigWord = mail
        bigCount = mcount
print(bigWord,bigCount)
