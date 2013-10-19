size = 21

grid = [ [ 1 for i in range(size) ] for j in range(size) ]

for y in range(size):
	for x in range(size):
		
		if(x > 0 and y > 0 ):
			grid[y][x] = grid[y-1][x] + grid[y][x-1]


print grid[size-1][size-1]