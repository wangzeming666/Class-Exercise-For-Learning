nameSet = set()
name = input("Please enter a name of students:")
while len(name):
    nameSet.add(name)
    name = input("Please enter a name of students(enter a Enter to quit):")
absentSet = set()
print("Let's have a roll call, enter y to show you are present")
for i in nameSet:
    print(i,'!')
    choice = input()
    if choice == 'y':
        pass
    else:
        absentSet.add(i)
print(absentSet)
