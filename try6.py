def min(a, b, c):
    if b > a:
        a, b = b, a
    if c > b:
        b, c = c, b
    if b > a:
        a, b = b, a
    return (c, a)

   
