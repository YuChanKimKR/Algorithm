import sys
input = sys.stdin.readline
#함수정하기앙기모띠씨발제발좆도리ㅏ
def merge_sort(arr, tmp, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, tmp, p, q)
        merge_sort(arr, tmp, q + 1, r)
        merge(arr, tmp, p, q, r)

def merge(arr, tmp, p, q, r):
    global count, result

    i, j, t = p, q + 1, 0
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t-1]
    
    while i <= q:
        tmp[t] = arr[i]
        i += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t-1]

    while j <= r:
        tmp[t] = arr[j]
        j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t-1]

    for i in range(t):
        arr[p + i] = tmp[i]

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1

merge_sort(A, [0] * N, 0, N - 1)

print(result)