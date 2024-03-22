N, M = map(int, input().split())  # N: 바구니의 개수, M: 방법의 개수

buckets = list(range(1, N + 1))  # 초기 바구니의 순서

# 방법의 개수(M)만큼 반복하여 바구니의 순서를 변경
for _ in range(M):
    i, j = map(int, input().split())  # 바꿀 바구니의 범위 i부터 j까지
    buckets[i - 1:j] = reversed(buckets[i - 1:j])  # 해당 범위의 바구니 순서를 역순으로 변경

# 최종적으로 바뀐 바구니의 순서를 출력
print(*buckets)