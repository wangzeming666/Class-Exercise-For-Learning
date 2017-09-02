def isprime(x):
    if x < 2:
        return False
    for i in range(2, x+1):
        if x % i == 0:
            return False
        if i > x // 2 + 1:
            return True

