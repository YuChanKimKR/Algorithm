import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def d(start, n, g):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        c, now = heapq.heappop(q)
        if c > dist[now]:
            continue
        
        for nxt, cost in g[now]:
            nc = c + cost
            if nc < dist[nxt]:
                dist[nxt] = nc
                heapq.heappush(q, (nc, nxt))
    
    return dist

n, e = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = d(1, n, g)
dist_v1 = d(v1, n, g)
dist_v2 = d(v2, n, g)

p1 = dist1[v1] + dist_v1[v2] + dist_v2[n]
p2 = dist1[v2] + dist_v2[v1] + dist_v1[n]

res = min(p1, p2)

if res >= INF:
    print(-1)
else:
    print(res)