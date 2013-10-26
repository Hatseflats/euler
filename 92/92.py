import math
def digits(nr):
        while nr:
            digit = nr % 10
            nr //= 10
            yield digit

def multi_coef(nr):
    d = list(digits(nr))
    u = set(d)
    counts = list(d.count(x) for x in u)

    mult = 1

    for x in map(math.factorial, counts):
        mult *= x

    return math.factorial(sum(counts)) // mult


def solution(max_nr):
    count = 0
    for i in range(1, max_nr):

        check = 0
        perm = True

        for d in list(digits(i))[::-1]:
            if 0 == d:
                continue
            if d < check:
                perm = False
                break
            check = d

        if not perm:
            continue

        nr = i

        while True:
            nr = sum([x**2 for x in digits(nr)])
            if nr == 1: 
                break
            if nr == 89:

                # filter out the zeroes since theyre not relevant
                num = int(''.join(map(str,[x for x in digits(i) if x != 0])))

                count += multi_coef(num)
                break

    return count

print(solution(10**7))



