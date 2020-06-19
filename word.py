word = input()

upr = 0
lwr = 0
for char in word :
    if char.islower() == True:
        lwr = lwr + 1
    if char.isupper() == True:
        upr = upr + 1

if upr > lwr :
    print(word.upper())
else:
    print(word.lower())

#print(word.lower())
