def min_len(arr, S):
    n = len(arr)
    l = 0
    curr_sum = 0
    
    #배열 길이 ㅈㄴ크게 설정해주기
    min_len = float('inf')

    for r in range(n):
        curr_sum += arr[r]

        while curr_sum >= S:
            min_len = min(min_len, r - l + 1)
            curr_sum -= arr[l]
            l += 1

    if min_len == float('inf'):
        return 0
    return min_len

N, S = map(int, input().split())
arr = list(map(int, input().split()))

print(min_len(arr, S))