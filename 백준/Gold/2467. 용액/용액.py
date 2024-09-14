def find(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    best_sum = float('inf')
    answer = (0, 0)
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if abs(current_sum) < abs(best_sum):
            best_sum = current_sum
            answer = (arr[left], arr[right])
        
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    
    return answer

n = int(input())
arr = list(map(int, input().split()))

result = find(arr)
print(result[0], result[1])