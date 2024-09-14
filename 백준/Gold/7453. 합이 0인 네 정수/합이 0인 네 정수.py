import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum_ab_counts = {}
for a in A:
    for b in B:
        sum_ab = a + b
        sum_ab_counts[sum_ab] = sum_ab_counts.get(sum_ab, 0) + 1

result = 0
for c in C:
    for d in D:
        sum_cd = c + d
        complement = -sum_cd
        if complement in sum_ab_counts:
            result += sum_ab_counts[complement]

print(result)
