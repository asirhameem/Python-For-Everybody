import re
lyric = input()

new = re.sub('WUB',' ',lyric)

print(new.lstrip(" "))
