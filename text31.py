def triangle(lines):
    LL = [[1]]
    for i in range(1,int(lines)):
        LL.append([(0 if j == 0 else LL[i-1][j-1]) + (0 if j == len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL

n = input("Please enter a number of high:")
LL = triangle(n)
for i in LL:
    print(str(str(i)).center(180))

