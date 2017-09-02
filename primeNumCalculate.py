primeNumList = []
num = int(input("Enter a number:"))
k = 0
while k == 0:
    for i in range(2,num//2+1):
        if num % i == 0:
            primeNumList.append(i)
            num /= i
        else:
            k = 1
for i in primeNumList:
    print(i,'*',end='')
print(num, '='end='')

