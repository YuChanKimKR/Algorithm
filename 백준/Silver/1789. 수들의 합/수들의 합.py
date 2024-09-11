S = int(input())

N = 0
total_sum = 0

while total_sum <= S:
    N += 1
    total_sum += N

print(N - 1)