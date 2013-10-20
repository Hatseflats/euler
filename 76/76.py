number = 100

table = []

for n in range(0, number+1):
    table.append([])

    row = table[len(table)-1]
    for p in range(0, number+1):
        if n == 0:
            row.append(0)
        elif p == 0:
            row.append(0)
        elif p > n:
            row.append(0)
        elif p == 1:
            row.append(1)
        else:
            row.append(table[n-1][p-1] + table[n-p][p])


print(sum(table[100])-1)


