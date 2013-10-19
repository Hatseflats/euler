from array import *
import math

prime = 3
counter = 2

while(counter != 10001):

	prime = prime + 2;
	isPrime = True

	for i in range(3, int(math.sqrt(prime)+1), 2):
		if(prime % i == 0):
			isPrime = False
			break

	if(isPrime):
		counter += 1
		print prime
		print counter





