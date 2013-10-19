numbers = {}

def Fib(n):
	if(n == 0): 					return 0
	elif(n == 1): 					return 1
	elif(numbers.get(n) != None): 	return numbers.get(n)
	else:							return Fib(n-1)	+ Fib(n-2)

n = 1
fib = 1

while(len(str(fib)) < 1000):
	fib = Fib(n)
	numbers[n] = fib
	n += 1	

print n-1, fib

