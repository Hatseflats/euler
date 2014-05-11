min_block_length = 3

cache = {}

def f(n):

    count = 0

    if n in cache:
        return cache[n]

    for position in range(n):
        for length in range(min_block_length, n+1):
            if position + length  <= n:
                count += 1 # the empty base case
                remainder = n - position - length - 1

                if remainder >= min_block_length:
                    count += f(remainder)

    cache[n] = count

    return count
# + 1 for the case where the entire row is empty
print(f(50) + 1)

