import math

def nthperm(n, m):
	data = range(0, n+1)
	nfac = math.factorial(len(data))
	answer = ""

	while len(data) > 0:
		pos = nfac / len(data)
		res = int(math.ceil(float(m) / pos))-1
		m = m % pos

		answer += str(data[res])

		del data[res]

		nfac = pos

	return answer

print nthperm(9, 1000000)

