List = []
n = 0
i = 5
while n < 5:	
	k = 0
	for j in range(1, i//2+1):
		if i % j == 0:
			k += j
	if k == i:
		List.append(i)
		n += 1
	i += 1

print(List)
