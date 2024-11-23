import sys
from collections import deque
sys.setrecursionlimit(100000)  # 충분히 큰 재귀 깊이 설정
input = sys.stdin.read

def dfs(tree, dp, n):
    stack = deque([1])  # 1번 노드부터 시작
    visited = [False] * (n + 1)
    order = []  # 탐색 순서 저장

    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        order.append(node)
        for child in tree[node]:
            if not visited[child]:
                stack.append(child)

    # DP 계산 (역순으로 처리)
    for node in reversed(order):
        dp[node][0] = 0
        dp[node][1] = 1
        for child in tree[node]:
            if dp[child][0] == -1:  # 부모 노드 방문 방지
                continue
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

# 입력 처리
data = input().splitlines()
n = int(data[0])

# 그래프 생성
tree = [[] for _ in range(n + 1)]
for i in range(1, n):
    u, v = map(int, data[i].split())
    tree[u].append(v)
    tree[v].append(u)

# DP 배열 초기화
dp = [[-1, -1] for _ in range(n + 1)]

# DFS로 DP 계산
dfs(tree, dp, n)

# 루트 노드 결과 출력
print(min(dp[1][0], dp[1][1]))
