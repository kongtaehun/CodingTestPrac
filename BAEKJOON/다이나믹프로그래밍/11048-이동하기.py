

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if i-1 >= 0 and j-1 >= 0:
                board[i][j] = board[i][j] + \
                    max(board[i-1][j], board[i][j-1], board[i-1][j-1])
            elif i-1 >= 0:
                board[i][j] = board[i][j] + board[i-1][j]
            elif j-1 >= 0:
                board[i][j] = board[i][j] + board[i][j-1]

    print(board[n-1][m-1])
