def ifDividesAll(num):
	for i in range(2,21):
		if num % i != 0:
			return False
	return True
num = 20
while True:
        print str(num)
        if ifDividesAll(num):
		break
	else:
		num = num + 1
print num
