
def dc(arr, b):
    if b == 1:
        return divid1000(arr)
    elif b % 2 == 0:
        return divid1000(powerArr(dc(arr, b//2), n))
    else:
        return divid1000(multiArr(powerArr(dc(arr, b//2), n), arr))


def multiArr(board1, board2):
    new_board = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new_board[i][j] += board1[i][x]*board2[x][j]
    return new_board


def powerArr(arr, n):
    new_board = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new_board[i][j] += arr[i][x]*arr[x][j]
    return new_board


def divid1000(board):
    for i in range(n):
        for j in range(n):
            board[i][j] = board[i][j] % 1000
    return board


def printArr(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


if __name__ == '__main__':
    n, b = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    printArr(dc(board, b))
