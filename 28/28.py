size = 1001

grid = [ [ None for i in range(size) ] for j in range(size) ]

dx, dy = 1, 0
x, y = 0, 0

for i in xrange(size**2, 0, -1):
	grid[y][x] = i

	nx, ny = x + dx, y + dy

	if (0 <= nx < size and 0 <= ny < size and grid[ny][nx] == None):
		x, y = nx, ny
	else:
		dx, dy = -dy, dx
		x, y =  x + dx, y + dy

diagonal_sum = -1

for c in range(size):
	diagonal_sum += grid[c][c]
	diagonal_sum += grid[c][size - c - 1]

print diagonal_sum


