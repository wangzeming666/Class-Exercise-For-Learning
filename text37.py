def jie(n):
    if n <= 1:
        return 1
    else:
        return n *jie(n-1)
print(jie(5))
