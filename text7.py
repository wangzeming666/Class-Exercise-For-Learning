k = 0
for i in range(2, 100):
	for k in range(2, i//2):
		while i % k == 0:
			k += 1
			continue
	if k == 0:
		print(i)
