import sys
input = sys.stdin.readline


def fishingShark(board, now):
    for i in range(n):
        if board[i][now][0] != 0:
            # 상어를 만났을 떄 낚시하기
            temp = board[i][now][0]
            board[i][now][0] = 0
            board[i][now][1] = 0
            board[i][now][2] = 0
            return temp
    return 0


def moveShark(board, new_board, x, y):
    s_size, direc, ori_speed = board[x][y]
    speed = ori_speed
    while speed > 0:
        if direc == 4:
            # 가장 왼쪽으로 보내자
            y = 1
            direc = 3
            speed -= y+1
        elif direc == 3:
            # 가장 오른쪽으로 보내자
            y = m-2
            direc = 4
            speed = m-y
        elif direc == 2:
            # 가장 왼쪽으로 보내자
            x = n-2
            direc = 1
            speed -= n-x
        elif direc == 1:
            x = 1
            direc = 2
            speed -= x+1
    if new_board[x][y] == 0:
        new_board[x][y] = [s_size, direc, ori_speed]
    else:
        if s_size > new_board[x][y][0]:
            new_board[x][y] = [s_size, direc, ori_speed]


def replaceShark(board):
    new_board = [[[0, 0, 0]]*(m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j][0] != 0:
                moveShark(board, new_board, i, j)
    return new_board


if __name__ == '__main__':

    # =========board만들기=============
    #n =세로, m=가로, k= 상어수
    n, m, k = map(int, input().split())
    answer = 0
    # 크기,방향,속력
    board = [[[0, 0, 0]for i in range(m)] for i in range(n)]
    for _ in range(k):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1][0] = z
        board[r-1][c-1][1] = d
        board[r-1][c-1][2] = s

    # =========낚시시작===============
    for now in range(m):
        # (now로 이동)
        # 낚시시작
        answer += fishingShark(board, now)
        board = replaceShark(board)
        # printBoard(board)
        # 상어이동시작
    print(answer)
