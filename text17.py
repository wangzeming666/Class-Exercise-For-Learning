List = []
num = input("Please enter a number:")
for i in range(len(num)):
	List.append(num[i])
for i in range(10):
	print(i, "times:", List.count(str(i)))
