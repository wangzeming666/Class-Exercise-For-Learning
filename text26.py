list1 = []
num = input("Please enter a number of list:")
while num:
    list1.append(num)
    num = input("Please enter a number of list(enter a Enter to quit):")
list2 = set()
numSet = set()
for i in list1:
    if i in list2:
        pass
    else:
        list2.add(i)
print(list2)

