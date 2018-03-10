x1 = int(input().strip())
x2 = int(input().strip())

d = abs(x1-x2)

n = d//2
rem = d%2

result = (1+n) * n

result += rem*(n+1)
print(result)
