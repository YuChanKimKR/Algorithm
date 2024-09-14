from itertools import combinations
from bisect import bisect_right

def find_sub_sums(arr):
    sub_sums = []
    n = len(arr)
    for i in range(n + 1):
        for comb in combinations(arr, i):
            sub_sums.append(sum(comb))
    return sub_sums

def solve():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))

    arr1 = arr[:n // 2]
    arr2 = arr[n // 2:]

    sub_sums1 = find_sub_sums(arr1)
    sub_sums2 = find_sub_sums(arr2)

    sub_sums2.sort()

    count = 0

    for s1 in sub_sums1:
        count += bisect_right(sub_sums2, c - s1)

    print(count)

solve()