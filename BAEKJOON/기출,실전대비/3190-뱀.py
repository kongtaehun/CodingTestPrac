# 사과없어지는 예외생각!
# 구현
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def printBoard(board):
    print('----------------')
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()
    print('----------------')


def setBoard():
    n = int(input())
    board = [['.']*(n+2) for i in range(n+2)]
    # 벽만들기
    for i in range(n+2):
        board[i][0] = '#'
        board[i][-1] = '#'
    for i in range(n+2):
        board[0][i] = '#'
        board[n+1][i] = '#'

    # 사과넣기
    for i in range(int(input())):
        a, b = map(int, input().split())
        board[a][b] = 'a'

    return board

# start


def start(moves):
    now_direc = 1
    snake = [[1, 1]]
    second = 0
    while True:
        second += 1
        snake = move(snake, now_direc)
        if not snake:
            return second
        # print(second)
        if len(moves) >= 1 and int(moves[0][0]) == second:
            # print(str(second)+"에 방향전환"+str(now_direc)+"에서", end=' ')
            now_direc = rotate(now_direc, moves[0][1])
            # print(str(now_direc)+"됨")
            moves.pop(0)


def failCondition(snake, headx, heady):

    if board[headx][heady] == '#':
        return True
    for i in snake:
        if headx == i[0] and heady == i[1]:
            return True

    return False

# move


def move(snake, direc):
    if failCondition(snake, snake[0][0] + dx[direc], snake[0][1] + dy[direc]):
        return False
    tempx = snake[0][0] + dx[direc]
    tempy = snake[0][1] + dy[direc]
    if board[tempx][tempy] == 'a':
        snake = [[tempx, tempy]]+snake
        board[tempx][tempy] = '.'
    else:
        snake = [[tempx, tempy]]+snake
        snake.pop()

    return snake
# rotate


def rotate(direc, rotateC):
    if rotateC == 'L':
        if direc == 0:
            direc = 3
        else:
            direc -= 1
    else:
        if direc == 3:
            direc = 0
        else:
            direc += 1
    return direc


if __name__ == '__main__':
    board = setBoard()
    moves = [list(map(str, input().split())) for i in range(int(input()))]
    print(start(moves))
