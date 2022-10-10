

def difuse(board):
    temp_board = [[0]*(m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != -1:
                now = board[i][j]
                cnt = 0
                if 0 <= i+1 < n and board[i+1][j] != -1:
                    temp_board[i+1][j] += now//5
                    cnt += 1
                if 0 <= j+1 < m and board[i][j+1] != -1:
                    temp_board[i][j+1] += now//5
                    cnt += 1
                if 0 <= i-1 < n and board[i-1][j] != -1:
                    temp_board[i-1][j] += now//5
                    cnt += 1
                if 0 <= j-1 < m and board[i][j-1] != -1:
                    temp_board[i][j-1] += now//5
                    cnt += 1
                temp_board[i][j] -= (now//5)*cnt
    for i in range(n):
        for j in range(m):
            board[i][j] += temp_board[i][j]
    # print(board)


def up_cycle(board, x):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    d = 0
    origin_x = x

    y = 1

    now = board[x][y]
    board[x][y] = 0
    while True:

        x = x+dx[d]
        y = y+dy[d]
        if x >= n or y >= m or 0 > x or 0 > y:
            x = x-dx[d]
            y = y-dy[d]

            d += 1
            x = x+dx[d]
            y = y+dy[d]
        if y == 0 and x == origin_x:
            break
        board[x][y], now = now, board[x][y]


def down_cycle(board, x):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    origin_x = x

    y = 1

    now = board[x][y]
    board[x][y] = 0
    while True:

        x = x+dx[d]
        y = y+dy[d]
        if x >= n or y >= m or 0 > x or 0 > y:
            x = x-dx[d]
            y = y-dy[d]

            d += 1
            x = x+dx[d]
            y = y+dy[d]
        if y == 0 and x == origin_x:
            break
        board[x][y], now = now, board[x][y]


def check(board):
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != -1:
                result += board[i][j]
    return result


def printB(board):
    for i in board:
        print(i)


def findAirCon(board):
    x1 = 0
    x2 = 0
    for i in range(n):
        if board[i][0] == -1:
            if x1 == 0:
                x1 = i
            else:
                x2 = i
    return x1, x2


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    x1, x2 = findAirCon(board)

    for i in range(t):
        difuse(board)
        up_cycle(board, x1)
        down_cycle(board, x2)
    print(check(board))
