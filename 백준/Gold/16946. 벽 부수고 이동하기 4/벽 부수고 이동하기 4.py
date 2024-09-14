from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().strip())) for _ in range(n)]

res = [[0] * m for _ in range(n)]
sz = {}
grp = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, id):
    q = deque([(x, y)])
    grp[x][y] = id
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0 and grp[nx][ny] == -1:
                grp[nx][ny] = id
                q.append((nx, ny))
                cnt += 1
    return cnt

gid = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 0 and grp[i][j] == -1:
            sz[gid] = bfs(i, j, gid)
            gid += 1

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            seen = set()
            cnt = 1
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and g[ni][nj] == 0:
                    grp_id = grp[ni][nj]
                    if grp_id not in seen:
                        cnt += sz[grp_id]
                        seen.add(grp_id)
            res[i][j] = cnt % 10

for i in range(n):
    print(''.join(map(str, res[i])))