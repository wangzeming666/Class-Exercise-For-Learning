def age(n):
    if n==0:
        return 1
    else:
        return age(n-1)+2
print(10+age(5))
