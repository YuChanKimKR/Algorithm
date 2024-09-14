import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
dp = [[-1]*c for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def valid(nx, ny, h):
    return 0 <= nx < r and 0 <= ny < c and grid[nx][ny] < h

def dfs(x, y):
    if x == r - 1 and y == c - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if valid(nx, ny, grid[x][y]):
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))