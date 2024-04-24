#내장함수 조합 이용
from itertools import combinations_with_replacement

N, M = map(int, input().split())

combs = combinations_with_replacement(range(1, N + 1), M)

for comb in combs:
    print(*comb)