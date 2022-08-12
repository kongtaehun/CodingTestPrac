# 완전탐색으로 가야할거같은데?
def type1(board):
    global result
    for i in range(n-2):
        for j in range(m-1):
            result = max(result, board[i][j] + board[i+1]
                         [j]+board[i+1][j+1]+board[i+2][j+1])
            result = max(result, board[i][j+1] + board[i+1]
                         [j]+board[i+1][j+1]+board[i+2][j])

    for i in range(n-1):
        for j in range(m-2):
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i+1][j+1]+board[i+1][j+2])
            result = max(result, board[i][j+2]+board[i]
                         [j+1]+board[i+1][j+1]+board[i+1][j])


def type2(board):
    global result
    for i in range(n-2):
        for j in range(m-1):
            result = max(result, board[i][j]+board[i+1]
                         [j]+board[i+2][j]+board[i+1][j+1])
            result = max(result, board[i][j+1]+board[i+1]
                         [j+1]+board[i+2][j+1]+board[i+1][j])

    for i in range(n-1):
        for j in range(m-2):
            result = max(result, board[i][j+1]+board[i+1]
                         [j]+board[i+1][j+1]+board[i+1][j+2])
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i][j+2]+board[i+1][j+1])


def type3(board):
    global result
    for i in range(n-2):
        for j in range(m-1):
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i+1][j+1]+board[i+2][j+1])
            result = max(result, board[i][j]+board[i+1]
                         [j]+board[i+2][j]+board[i+2][j+1])
            result = max(result, board[i][j+1]+board[i+1]
                         [j+1]+board[i+2][j+1]+board[i+2][j])
            result = max(result, board[i+1][j]+board[i+2]
                         [j]+board[i][j]+board[i][j+1])

    for i in range(n-1):
        for j in range(m-2):
            result = max(result, board[i+1][j]+board[i+1]
                         [j+1]+board[i+1][j+2]+board[i][j+2])
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i][j+2]+board[i+1][j+2])
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i][j+2]+board[i+1][j])
            result = max(result, board[i+1][j]+board[i+1]
                         [j+1]+board[i+1][j+2]+board[i][j])


def type4(board):
    global result
    for i in range(n):
        for j in range(m-3):
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i][j+2]+board[i][j+3])

    for i in range(n-3):
        for j in range(m):
            result = max(result, board[i][j]+board[i+1]
                         [j]+board[i+2][j]+board[i+3][j])


def type5(board):
    global result
    for i in range(n-1):
        for j in range(m-1):
            result = max(result, board[i][j]+board[i]
                         [j+1]+board[i+1][j]+board[i+1][j+1])


if __name__ == '__main__':
    n, m = map(int, input().split())
    result = 0
    board = [list(map(int, input().split())) for i in range(n)]
    type1(board)
    type2(board)
    type3(board)
    type4(board)
    type5(board)
    print(result)
