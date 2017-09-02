def zhishu(num):
	for i in range(2, num):
		if num % i == 0:
			break
	else:
                return 1
	return 0

x = 2
while True:
        if zhishu(x):
                if zhishu(2**x-1):
                        print((2**x-1)*(2**(x-1)))
        x += 1
