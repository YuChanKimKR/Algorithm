N = int(input())
arr = list(map(int, input().split()))

def sum_max(arr):
    sum = arr[0]
    max = arr[0]

    for i in range(1, N):
        sum += arr[i]
        if sum < arr[i]:
            sum = arr[i]
        if sum > max:
            max = sum

    return max

print(sum_max(arr))