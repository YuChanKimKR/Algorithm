N, M = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            temp_sum = numbers[i] + numbers[j] + numbers[k]
            if temp_sum <= M and temp_sum > answer:
                answer = temp_sum

print(answer)