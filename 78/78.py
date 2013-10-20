import math

def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = [1]

n = 1

while True:
    r, i = 0, 0
    while True:
        k = pentagonal(math.floor(i/2) + 1) if i % 2 == 0 else pentagonal(-1 * math.floor(i/2) - 1)

        if k > n: 
            break

        r += (1 if i % 4 < 2 else -1)  * partitions[int(n - k)]
        i += 1

    if r % (10**6) == 0:
        print(len(partitions), r)
        break

    partitions.append(r)

    n += 1
