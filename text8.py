i = 2
k = 2
while i <= 100:
    while k <= i // 2:
        if i % k == 0:
            
            break
        if k > (i // 2):
            print(i)
        k += 1
    k = 2
    i += 1
