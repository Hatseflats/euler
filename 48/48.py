result = 0

for i in range(1, 1001):
	result += i**i

result = str(result)
result_length = len(result)
digits = ""

for i in range(0, 10):
	print i
	digits += result[result_length-10+i]

print result
print digits

