n, m = map(int, input().split())

first = []
second = []

for _ in range(n):
    first.append(input())

for _ in range(m):
    second.append(input())

res = set(first).intersection(second)

print(len(res))
for r in sorted(res):
    print(r)