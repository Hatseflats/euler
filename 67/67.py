import string

f = open('triangle.txt','r')
triangle = []

for line in f:
	triangle.append(map(int,string.strip(line).split(" ")))

f.close()

for y in range(len(triangle)-2, -1, -1):
	for x in range(len(triangle[y])):
		if(triangle[y+1][x] > triangle[y+1][x+1]):
			triangle[y][x] += triangle[y+1][x]
		else:
			triangle[y][x] += triangle[y+1][x+1]

print triangle[0][0]
