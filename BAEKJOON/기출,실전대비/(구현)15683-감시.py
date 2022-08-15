import copy
from itertools import product, permutations
# 방법1 : 최대cctv의 커버영역을 cctv하나하나 구한다
# 방법2 : 1번 -> 4방향
#   2번 -> 2방향
#   3번 -> 4밫향
#   4번 -> 4방향
# 카메라별로 백트래킹하여 모든 경우의 수를 결정


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()


def upChange(board, x, y):
    for x_ in range(x-1, -1, -1):
        if board[x_][y] == 0:
            board[x_][y] = 7
        elif board[x_][y] == 6:
            break
        else:
            continue


def downChange(board, x, y):
    for x_ in range(x, n):
        if board[x_][y] == 0:
            board[x_][y] = 7
        elif board[x_][y] == 6:
            break
        else:
            continue


def leftChange(board, x, y):
    for y_ in range(y-1, -1, -1):
        if board[x][y_] == 0:
            board[x][y_] = 7
        elif board[x][y_] == 6:
            break
        else:
            continue


def rightChange(board, x, y):
    for y_ in range(y, m):
        if board[x][y_] == 0:
            board[x][y_] = 7
        elif board[x][y_] == 6:
            break
        else:
            continue


def setCctv(board, cctv, position):
    for i in range(len(cctv)):
        if position[i] == 0:
            if cctv[i][0] == 1:
                upChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 2:
                upChange(board, cctv[i][1], cctv[i][2])
                downChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 3:
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 4:
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            else:
                downChange(board, cctv[i][1], cctv[i][2])
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
        elif position[i] == 1:
            if cctv[i][0] == 1:
                rightChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 2:
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 3:
                downChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 4:
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                downChange(board, cctv[i][1], cctv[i][2])
            else:
                downChange(board, cctv[i][1], cctv[i][2])
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
        elif position[i] == 2:
            if cctv[i][0] == 1:
                downChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 2:
                upChange(board, cctv[i][1], cctv[i][2])
                downChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 3:
                downChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 4:
                downChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            else:
                downChange(board, cctv[i][1], cctv[i][2])
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
        elif position[i] == 3:
            if cctv[i][0] == 1:
                leftChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 2:
                leftChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 3:
                upChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            elif cctv[i][0] == 4:
                upChange(board, cctv[i][1], cctv[i][2])
                downChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])
            else:
                downChange(board, cctv[i][1], cctv[i][2])
                upChange(board, cctv[i][1], cctv[i][2])
                rightChange(board, cctv[i][1], cctv[i][2])
                leftChange(board, cctv[i][1], cctv[i][2])


def countZero(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    origin_board = copy.deepcopy(board)
    cctv = []
    position = []
    # 카메라의 영역을 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != 6:
                cctv.append((board[i][j], i, j))
    position = [0, 1, 2, 3]
    result = int(1e9)
    temp = list(product(position, repeat=len(cctv)))
    for pos in temp:
        setCctv(board, cctv, pos)
        # printBoard(board)
        result = min(countZero(board), result)
        board = copy.deepcopy(origin_board)
    print(result)
