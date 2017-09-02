a, b, n, k = 1, 1, 0, 0
while n < 20:
	b, a = a, a + b
	k += a / b
	n += 1
print(k)
