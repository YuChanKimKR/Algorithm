N, M = map(int, input().split())

# 행렬 A 입력
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# 행렬 B 입력
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

# 두 행렬을 더한 결과 계산 및 출력
for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(A[i][j] + B[i][j])
    print(*result_row)