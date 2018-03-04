Q = int(input().strip())

def g(n):
    if n < 10:
        return n
    else:
        return g(f(n))

def f(n):
    prod = 1
    while n > 0:
        i = n % 10
        if i > 1:
            prod *= i
        n = n // 10
    return prod

for q in range(Q):
    l, r, k = list(map(int, input().strip().split(' ')))
    count = 0
    for x in range(l, r+1):
        if g(x) == k:
            count += 1
    print(count)
