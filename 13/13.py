
total = 0
power = 49

lines = list(map(lambda line: line.strip(), open('numbers.txt')))

for i in range(11):
    for num in lines:
        total += (int(num[i]) * (10**power))

    power -= 1

print(str(total)[0:10])
