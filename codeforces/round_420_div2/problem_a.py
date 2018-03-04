def isClean(n, grid, rows, cols):
    for i in range(n):
        for j in range(n):
            idx = i*n+j
            if grid[idx] != 1:
                isValid = False
                for row_v in rows[i]:
                    if grid[idx]-row_v in cols[j]:
                        isValid = True
                        break
                if not isValid:
                    print('No')
                    return
    print('Yes')

n = int(input().strip())
grid = []
for i in range(n):
    row = list(map(int, input().strip().split(' ')))
    grid.extend(row)

rows = [set() for _ in range(n)]
cols = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        idx = i*n+j
        rows[i].add(grid[idx])
        cols[j].add(grid[idx])

isClean(n, grid, rows, cols)
