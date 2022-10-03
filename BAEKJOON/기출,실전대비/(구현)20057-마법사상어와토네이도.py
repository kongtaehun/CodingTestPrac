dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 규칙
# 1 1 2 2 3 3 4 4 5 5 6 6 6 .... 마지막하나더 N-1까지함
# 왼 아 오 위 왼 아 오 위


def getTorMoves():
    moves = []
    d = 0
    for i in range(1, n):
        moves.append((i, d % 4))
        d += 1
        moves.append((i, d % 4))
        d += 1
    moves.append((i, d % 4))
    return moves


def check(board):
    sum = 0
    for i in range(2, 2+n):
        for j in range(2, 2+n):
            sum += board[i][j]

    return sum


def move(too, dirc):

    nx, ny = too

    sand = board[nx][ny]
    board[nx][ny] = 0
    a = sand - 2*int(sand*(0.02)) - 2*int(sand*(0.1)) - 2 * \
        int(sand*(0.07))-2*int(sand*(0.01)) - int(sand*(0.05))
    temp_board = [[0, 0, int(sand*(0.02)), 0, 0],
                  [0, int(sand*(0.1)), int(sand*(0.07)), int(sand*(0.01)), 0],
                  [int(sand*(0.05)), a, 0, 0, 0],
                  [0, int(sand*(0.1)), int(sand*(0.07)), int(sand*(0.01)), 0],
                  [0, 0, int(sand*(0.02)), 0, 0]
                  ]

    # 왼 아 오 위
    # dirc == 0일 땐 그대로
    if dirc == 1:
        # 반시계
        temp_board = list(map(list, zip(*temp_board)))[::-1]
    elif dirc == 2:
        temp_board = list(map(list, zip(*temp_board)))[::-1]
        temp_board = list(map(list, zip(*temp_board)))[::-1]
    elif dirc == 3:
        temp_board = list(map(list, zip(*temp_board[::-1])))
    temp_idx_x = 0
    temp_idx_y = 0
    for i in range(nx-2, nx+3):
        for j in range(ny-2, ny+3):
            board[i][j] += temp_board[temp_idx_x][temp_idx_y]
            temp_idx_y += 1
        temp_idx_y = 0
        temp_idx_x += 1


if __name__ == '__main__':
    n = int(input())

    board = [list(map(int, input().split())) for i in range(n)]
    # padding추가
    board = [[0]*n] + [[0]*n] + board + [[0]*n]+[[0]*n]
    for i in range(len(board)):
        board[i] = [0, 0]+board[i]+[0, 0]

    init_sand = check(board)

    mid = (n+4)//2
    moves = getTorMoves()
    now = [mid, mid]

    for cnt, dirc in moves:
        for _ in range(cnt):
            # print('from'+str(now))

            now[0] = now[0]+dx[dirc]
            now[1] = now[1]+dy[dirc]
            # print('to'+str(now))
            move(now, dirc)
    # print(board)

    after_sand = check(board)
    print(init_sand-after_sand)
