
import sys
input = sys.stdin.readline
N = 9


def countZero(board):
    count = 0
    zero_loc = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count += 1
                zero_loc.append((i, j))
    return count, zero_loc


flag = False


def bt(depth):  # depth => 0인 곳의 배열인덱스
    global flag
    if flag:
        return
    if depth == len(zero_loc):
        printArr(board)
        flag = True
        return

    for i in range(1, N+1):
        if check(depth, i):
            board[zero_loc[depth][0]][zero_loc[depth][1]] = i
            bt(depth+1)
            board[zero_loc[depth][0]][zero_loc[depth][1]] = 0


def printArr(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


def check(depth, value):
    x = zero_loc[depth][0]
    y = zero_loc[depth][1]

    for i in range(N):
        if value == board[x][i]:
            return False

    for i in range(N):
        if value == board[i][y]:
            return False

    # 8방향 체크
    for i in range(3*(x // 3), 3*(x // 3)+3):
        for j in range(3*(y // 3), 3*(y // 3)+3):

            if value == board[i][j]:
                return False

    return True


if __name__ == '__main__':
    board = [list(map(int, input().split())) for i in range(N)]
    # 0인 위치 저장하는 함수실행
    max_depth, zero_loc = countZero(board)
    bt(0)

