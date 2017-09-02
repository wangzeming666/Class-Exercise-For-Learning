import re
f = open('whodata.txt', 'r')
for eachline in f:
    print(re.split(r'\s\s+', eachline))
f.close()
