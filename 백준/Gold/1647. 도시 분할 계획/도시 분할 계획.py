import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:                  # 노드 n의 부모노드가 자기자신이 아니면
        parent[n] = find(parent[n])     # 노드 n의 부모노드 = 최상위 부모노드 탐색 재귀함수
    return parent[n]                    # 현재노드 n의 최상위 부모노드 return

def union(a, b):
    a = find(a)         # 노드 a의 최상위 노드 탐색
    b = find(b)         # 노드 b의 최상위 노드 탐색
    if a < b:           # a < b 이면
        parent[b] = a   # 노드b의 부모노드 a로 갱신
    else:               # a > b 이면
        parent[a] = b   # 노드a의 부모노드 b로 갱신


N, M = map(int, input().split())

edges = []
parent = list(range(N + 1))
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

answer = 0
last_edge = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        last_edge = c
print(answer - last_edge)