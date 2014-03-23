# 1*1 = 1 rectangle
# 1*2 = 3 rectangles
# 1*3 = 6 rectangles

# 1*n = n + (n - 1) + ( n - 2) ... + 1 = n(n+1) / 2

# 2*n = n(n+1) / 2 + n(n+1) / 2 + n(n+1) / 2
# (once for the first row, once for the second row and once for both of them together)
# m*n = (n(n+1) / 2) * (m(m+1) / 2)

target = 2*10**6

r = 0

distance = None;
closestn = 0
closestm = 0;

n = 0
while True:
    n += 1
    m = 0
    while True:
        m+= 1
        rectangles = (m*(m+1) // 2) * (n*(n+1) // 2)

        if distance is None or abs(target - rectangles) < distance:
            distance = abs(target - rectangles)
            closestm = m
            closestn = n
            
        if rectangles > target:
            break

    if n == m:
        break

print(closestn * closestm)