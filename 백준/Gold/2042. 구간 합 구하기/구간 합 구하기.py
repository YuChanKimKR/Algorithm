from math import ceil, log2

# 입력
N, M, K = map(int, input().split())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())

# 트리 크기 설정
tree_size = 2 ** (ceil(log2(N)) + 1)
tree = [0] * tree_size

def build_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_tree(node * 2, start, mid)
        build_tree(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

#구간 합 구하기
def summary(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_sum = summary(node * 2, start, mid, left, right)
    right_sum = summary(node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum

#입력값으로 값 바꾸기
def update(node, start, end, idx, val):
    if start == end:
        arr[idx] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(node * 2, start, mid, idx, val)
        else:
            update(node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

build_tree(1, 0, N - 1)

for _ in range(M + K):
    query_type, a, b = map(int, input().split())
    if query_type == 1:
        update(1, 0, N - 1, a - 1, b)
    elif query_type == 2:
        print(summary(1, 0, N - 1, a - 1, b - 1))