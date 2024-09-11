import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

filtered = [w for w in words if len(w) >= m]
count = Counter(filtered)

result = sorted(count.keys(), key=lambda x: (-count[x], -len(x), x))

for w in result:
    print(w)