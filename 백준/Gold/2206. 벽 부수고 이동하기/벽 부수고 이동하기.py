from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m, graph):
    queue = deque()
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while queue:
        x, y, broken = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                elif graph[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    queue.append((nx, ny, 1))
    
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(n, m, graph))
