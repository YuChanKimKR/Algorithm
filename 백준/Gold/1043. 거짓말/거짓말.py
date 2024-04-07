import sys

input = sys.stdin.readline

N, M = map(int, input().split())

input_truth = list(map(int, input().strip().split()))
truth = set(input_truth[1:])

party = []
for i in range(M):
    temp = list(map(int, input().strip().split()))
    party.append(temp)


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N + 1)]

# 각 파티 참가자들을 그룹핑
for i in range(M):
    for j in range(1, len(party[i])):
        union(party[i][j], party[i][1], parent)

# 진실을 아는 사람들과 같은 그룹에 속하는 파티 참가자들을 모두 찾음
for i in range(1, N + 1):
    if i in truth:
        for j in range(1, N + 1):
            if find(j, parent) == find(i, parent):
                truth.add(j)

count = M

# 과장된 이야기를 할 수 있는 파티의 수 계산
for i in range(M):
    for j in range(1, len(party[i])):
        if party[i][j] in truth:
            count -= 1
            break

print(count)