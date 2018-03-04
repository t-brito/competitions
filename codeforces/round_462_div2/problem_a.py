m,n = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

a.sort()
b.sort()

if b[0] >= 0:
    a = a[:-1]
elif b[-1] <= 0:
    a = a[1:]
elif a[-1]*b[-1] > a[0]*b[0]:
    a = a[:-1]
else:
    a = a[1:]

if a[0] >= 0:
    bfinal = max(a[-1]*b[-1],a[0]*b[-1])
elif a[-1] <= 0:
    bfinal = max(a[0]*b[0],a[-1]*b[0])
else:
    bfinal = max(a[-1]*b[-1], a[0]*b[0])

print(bfinal)
