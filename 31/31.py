coins = [1,2,5,10,20,50,100,200]

def c(coins, index, capacity):
    if capacity == 0:
        return 1
    if capacity < 0 or index < 0:
        return 0

    a = c(coins, index-1, capacity)
    b = c(coins, index, capacity-coins[index])

    return a+b

print(c(coins, len(coins)-1, 200))

