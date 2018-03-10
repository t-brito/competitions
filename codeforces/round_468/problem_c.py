_ = input()
X = list(map(int, input().strip().split(' ')))

total = len(X)

dX = {}
for x in X:
    if x in dX:
        dX[x] += 1
    else:
        dX[x] = 1

minX=min(dX.keys())
maxX=max(dX.keys())

if maxX - minX == 2:
    midX = (maxX+minX)//2
    if min(dX[minX], dX[maxX]) >= dX[midX]//2: # cancel max/min
        rem = min(dX[minX], dX[maxX])
        dX[minX] -= rem
        dX[maxX] -= rem
        dX[midX] += rem*2
        strikeoff = total - rem*2
    else:   # cancel middle pairs
        rem = dX[midX]-dX[midX]%2
        dX[midX] -= rem
        dX[maxX] += rem//2
        dX[minX] += rem//2
        strikeoff = total - rem
# elif max(X) - min(X) == 1:
    # if dX[minX] >= dX[maxX]:
    #     rem = dX[minX]-dX[minX]%2
    #     dX[minX] -= rem
    #     dX[minX+1] += rem//2
    #     dX[minX-1] = rem//2
    # else:
    #     rem = dX[maxX]-dX[maxX]%2
    #     dX[maxX] -= rem
    #     dX[maxX+1] = rem//2
    #     dX[maxX-1] -= rem//2
    # strikeoff = total - rem
else:
    # rem = dX[minX]-dX[minX]%2
    # dX[minX] -= rem
    # dX[minX+1] = rem//2
    # dX[minX-1] = rem//2
    # strikeoff = total - rem
    strikeoff=total

print(strikeoff)
for k in dX.keys():
    for i in range(dX[k]):
        print(k, end=' ')
print()
