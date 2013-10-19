def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

answer = 0;

for ch in str(factorial(100)):
	answer += int(ch)

print answer


