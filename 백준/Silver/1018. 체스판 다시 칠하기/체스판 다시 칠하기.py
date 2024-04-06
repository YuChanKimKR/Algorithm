def count_repaints(board):
    repaints_w = 0  # 흰색으로 시작하는 경우
    repaints_b = 0  # 검은색으로 시작하는 경우
    
    # 체스판을 검사하면서 다시 칠해야 하는 경우를 센다
    for i in range(8):
        for j in range(8):
            # 흰색으로 시작하는 경우
            if (i + j) % 2 == 0:
                if board[i][j] == 'B':
                    repaints_w += 1
            # 검은색으로 시작하는 경우
            else:
                if board[i][j] == 'W':
                    repaints_w += 1
    
    # 체스판을 검사하면서 다시 칠해야 하는 경우를 센다
    for i in range(8):
        for j in range(8):
            # 검은색으로 시작하는 경우
            if (i + j) % 2 == 0:
                if board[i][j] == 'W':
                    repaints_b += 1
            # 흰색으로 시작하는 경우
            else:
                if board[i][j] == 'B':
                    repaints_b += 1
    
    # 두 경우 중에서 최소값을 반환한다
    return min(repaints_w, repaints_b)

# 입력 받기
N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaints = float('inf')  # 최소 다시 칠해야 하는 정사각형 개수를 저장할 변수

# 보드를 탐색하면서 8x8 크기의 체스판을 모두 확인한다
for i in range(N - 7):
    for j in range(M - 7):
        # 현재 위치에서 8x8 크기의 부분 보드를 가져온다
        sub_board = [row[j:j+8] for row in board[i:i+8]]
        repaints = count_repaints(sub_board)  # 다시 칠해야 하는 정사각형 개수를 계산한다
        min_repaints = min(min_repaints, repaints)  # 최소값을 갱신한다

print(min_repaints)