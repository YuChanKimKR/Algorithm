import sys
input = sys.stdin.read
data = input().split()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

V, E = int(data[0]), int(data[1])
edges = []
idx = 2

for _ in range(E):
    a, b, weight = map(int, data[idx:idx+3])
    edges.append((weight, a, b))
    idx += 3

edges.sort()

parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)

mst_weight = 0
for weight, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        mst_weight += weight

print(mst_weight)