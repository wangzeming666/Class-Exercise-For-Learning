def isprime(y, x=2):
    if x < 2:
        return False
    if y < 2:
        return False
    list1 = []
    for i in range(x, y):
        for j in range(2, i // 2 + 2):
            if i % j == 0:
                break
            if j > i // 2:
                list1.append(i)
    return list1
x = input("Please enter a starting number to calculate prime number:")
y = input("And the end:")
print(isprime(y, x))
print(isprime(10))
print(isprime(100))
print(isprime(200))

