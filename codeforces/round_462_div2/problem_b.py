n = int(input())

if n > 36:
    print(-1)
else:
    s = ''
    for i in range(n // 2):
        s += '8'
    if n % 2 == 1:
        s += '4'
    print(s)
