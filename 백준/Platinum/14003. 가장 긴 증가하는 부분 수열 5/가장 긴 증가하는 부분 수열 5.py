from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

lis = []
indices = [0] * n
parent = [-1] * n

for i in range(n):
    if not lis or a[i] > lis[-1]:
        lis.append(a[i])
        indices[i] = len(lis) - 1
    else:
        pos = bisect_left(lis, a[i])
        lis[pos] = a[i]
        indices[i] = pos

lis_length = len(lis)
result = []
cur_index = lis_length - 1

for i in range(n - 1, -1, -1):
    if indices[i] == cur_index:
        result.append(a[i])
        cur_index -= 1

print(lis_length)
print(' '.join(map(str, result[::-1])))