#####  My system doesn't allow me to use Chinese
#####  There is a 'set()' funcsion that has not learnt.
#####  But I don't have any other way.


k = set() 
k.add(2)
for i in range(2, 100):
	for j in range(2,50):
		if i % j == 0:
			break
		if j > i // 2:
			k.add(i)
print(k)

