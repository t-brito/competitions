from math import log

n, a, b = map(int, input().strip().split(' '))

teams = sorted((a-1,b-1))

R = int(log(n, 2))
div = n//2

for r in range(R,0,-1):
    if teams[0] < div and teams[1] >= div:
        if r == R:
            print('Final!')
        else:
            print(r)
        break

    teams[0] %= div
    teams[1] %= div

    div //= 2
