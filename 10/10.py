max_prime = 2000000
numbers = [True] * max_prime
prime_sum = 0

for z in range(2, max_prime**1/2):
	for i in range(z*z, max_prime, z):
		numbers[i] = False

for i in range(2, max_prime):
	if numbers[i]:
		prime_sum += i

print prime_sum