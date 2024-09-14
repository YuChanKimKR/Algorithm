def count_trailing_zeros(N):
    count = 0
    while N >= 5:
        count += N // 5
        N //= 5
    return count

# 입력 받기
N = int(input())

# 결과 출력
print(count_trailing_zeros(N))
