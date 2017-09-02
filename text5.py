i = 0
while i <= 30:

    if i % 2 == 0:
        print(i, sep=' ', end=' ')
    i += 1

print()
print()
print()
print()



i = 65
k = 0
while i < 91:
    print(chr(i), sep=' ', end=' ')
    k += 1
    if k % 5 == 0:
        print()
    i += 1
print()
print()
print()
print()


i = 65
j = 97
k = 0
while i < 91:
    print(chr(i), chr(j), sep=' ', end=' ')
    k += 1
    if k % 5 == 0:
        print()
    i += 1
    j += 1
print()
print()
print()
print()


i = int(input("Please enter a number for beginning:"))
j = int(input("Please enter a number for ending:"))
while i <= j:
    print('%3d %3o %3x' %(i, i, i), chr(i), sep=' ', end=' ')
    print()
    i += 1

