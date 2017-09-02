import random
list2 = [[],[],[]]
k = 54
while k > 0:
    list1 = []
    for i in range(1,11):
        for j in ['redsq', 'blacksq', 'redpea', 'blackpea']:
            list1.append(j+str(i))
    for i in ('J','Q', 'K'):
        for j in ['redsq', 'blacksq', 'redpea', 'blackpea']:
            list1.append(j+i)
    list1.append('Queen')
    list1.append('King')
    for i in range(18):
        for j in range(3):
            l = random.choice(list1)
            list2[j].append(l)
            list1.pop(list1.index(l))
            k -= 1


for i in range(3):
    sorted(list2[i])
    print(list2[i])
    
