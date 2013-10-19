result = 0
for m in range (1, 1000, 1):
	for n in range (m+1, 1000, 1):
		a = n * n - m * m
		b = 2 * n * m
		c = n * n + m * m

		if(a+b+c == 1000):
			result = a*b*c
			break;

	if(result != 0):
		break;

print result