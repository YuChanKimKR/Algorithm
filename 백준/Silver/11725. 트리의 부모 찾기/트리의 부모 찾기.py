import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, parent):
    for neighbor in tree[node]:
        if parent_node[neighbor] == 0:
            parent_node[neighbor] = node
            dfs(neighbor, node)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent_node = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, 0)

for i in range(2, n + 1):
    print(parent_node[i])