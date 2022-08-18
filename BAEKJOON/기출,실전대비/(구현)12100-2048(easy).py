from itertools import product
MOVES = ['up', 'down', 'left', 'right']

# 왼쪽으로 붙혀버림


def rotateBoard(board):
    temp_board = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp_board[i][j] = board[j][i]
    return temp_board


def lineMove(line):
    temp_line = []
    prev = 0
    for i in range(n):
        if line[i] != 0:
            if prev == line[i]:
                temp_line.pop()
                temp_line.append(2*prev)
                prev = 0
            else:
                temp_line.append(line[i])
                prev = line[i]

    for i in range(n-len(temp_line)):
        temp_line.append(0)
    return temp_line


def doMove(board, direc):
    temp_board = []
    if direc == 'left':
        for i in range(n):
            temp_board.append(lineMove(board[i]))
    elif direc == 'right':
        for i in range(n):
            board[i].reverse()
            temp = lineMove(board[i])
            temp.reverse()
            temp_board.append(temp)
    elif direc == 'up':
        board = rotateBoard(board)
        for i in range(n):
            temp_board.append(lineMove(board[i]))
        temp_board = rotateBoard(temp_board)
    else:
        board = rotateBoard(board)
        for i in range(n):
            board[i].reverse()
            temp = lineMove(board[i])
            temp.reverse()
            temp_board.append(temp)
        temp_board = rotateBoard(temp_board)
    return temp_board


def gameStart(board, move):
    result = 0
    for i in move:
        board = doMove(board, i)
        max_val = max(map(max, board))
        result = max(result, max_val)
    return result


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    for m in list(product(MOVES, repeat=5)):
        answer = max(gameStart(board, m), answer)
    print(answer)
