# 9x9 격자 입력 받기
grid = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_row = 0
max_col = 0

# 격자 순회하면서 최댓값과 위치 찾기
for i in range(9):
    for j in range(9):
        if max_value <= grid[i][j]:
            max_row = i + 1
            max_col = j + 1
            max_value = grid[i][j]

# 최댓값과 위치 출력
print(max_value)
print(max_row, max_col)