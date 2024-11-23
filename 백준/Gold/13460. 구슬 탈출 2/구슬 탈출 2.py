from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
board = [list(row) for row in data[1:]]

red, blue, hole = None, None, None

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'O':
            hole = (i, j)

def move(x, y, dx, dy, board):
    count = 0 
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(board, red, blue, hole):
    n, m = len(board), len(board[0])
    queue = deque([(red, blue, 0)])  # ((rx, ry), (bx, by), moves)
    visited = set()
    visited.add((red, blue))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (rx, ry), (bx, by), moves = queue.popleft()

        if moves >= 10:
            return -1

        for dx, dy in directions:
            nrx, nry, r_count = move(rx, ry, dx, dy, board)
            nbx, nby, b_count = move(bx, by, dx, dy, board)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return moves + 1

            if (nrx, nry) == (nbx, nby):
                if r_count > b_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if ((nrx, nry), (nbx, nby)) not in visited:
                visited.add(((nrx, nry), (nbx, nby)))
                queue.append(((nrx, nry), (nbx, nby), moves + 1))

    return -1

result = bfs(board, red, blue, hole)

print(result)