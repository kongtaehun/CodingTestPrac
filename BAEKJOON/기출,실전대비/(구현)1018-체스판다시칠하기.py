dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def setBoard(n, m, a):
    board = [['0']*(m) for i in range(n)]
    board[0][0] = a
    for i in range(1, m):
        board[0][i] = 'W' if board[0][i-1] == 'B' else 'B'

    for i in range(1, n):
        for j in range(m):
            board[i][j] = 'W' if board[i-1][j] == 'B' else 'B'
    return board


def compareBoard(x, y, origin, board):
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if origin[i][j] != board[i-x][j-y]:
                cnt += 1
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    origin_board = [list(input()) for i in range(n)]
    answer = int(1e9)
    W_board = setBoard(8, 8, 'W')
    B_board = setBoard(8, 8, 'B')
    for start_x in range(n-8+1):
        for start_y in range(m-8+1):
            answer = min(answer, compareBoard(
                start_x, start_y, origin_board, W_board))
            answer = min(answer, compareBoard(
                start_x, start_y, origin_board, B_board))
    print(answer)
