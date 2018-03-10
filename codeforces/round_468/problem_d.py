n = int(input().strip())
F = tuple(map(int, input().strip().split(' ')))

oldTree = {}
newTree = {}
collected = 0
for i in range(1, n+1):
    oldTree[i] = 1

while (sum(oldTree.values()) > 0):
    collected += oldTree[1]
    for i in range(1, n+1):
        newTree[i] = 0

    for i in range(0, n-1):
        newTree[F[i]] += oldTree[i+2]
        newTree[F[i]] %= 2

    oldTree = newTree.copy()
print(collected)
