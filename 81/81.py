import string

matrix = []

f = open('matrix.txt','r')

for line in f:
	matrix.append(map(int, line.split(',')))

f.close()

size = len(matrix)

for y in range(size):
	for x in range(size):
		if(y == 0 and 0 < x < size):
			matrix[y][x] += matrix[y][x-1]
		elif(x == 0 and 0 < y < size):
			matrix[y][x] += matrix[y-1][x]
		elif x > 0 and y > 0:
			if((matrix[y-1][x] < matrix[y][x-1])):
				matrix[y][x] += matrix[y-1][x]
			else:
				matrix[y][x] += matrix[y][x-1]

print matrix[size-1][size-1]