num = input('Please enter a number:')
if num.isdigit():
	k, half_length = 0, len(num) // 2
	for i in range(half_length):
		if num[i] == num[-i-1]:k += 1	
	if k == half_length:print("It's a symmetry.")
else:
	print("It's not a symmetry!")


