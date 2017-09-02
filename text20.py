num = input("Please enter a number:")
if num.isdigit():
	if num == num[:: -1]:
		print("True")
	else:
		print("False")
else:
	print("False")

