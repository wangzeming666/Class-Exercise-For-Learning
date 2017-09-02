def jie(n):
        if n<=1:
                return 1
        else:
                return n*jie(n-1)
print(sum(map(jie,range(1,21))))
