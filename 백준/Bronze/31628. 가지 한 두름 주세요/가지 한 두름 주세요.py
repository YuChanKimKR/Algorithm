def check(grid):
    for row in grid:
        if all(x == row[0] for x in row):
            return True
    for c in range(10):
        col = [grid[r][c] for r in range(10)]
        if all(x == col[0] for x in col):
            return True
    return False

grid = [input().split() for _ in range(10)]

print(1 if check(grid) else 0)