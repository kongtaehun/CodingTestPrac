if __name__ == '__main__':
    INF = int(1e9)
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    dp_max = [[0]*(3) for i in range(n)]
    for i in range(3):
        dp_max[0][i] = board[0][i]
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp_max[i][j] = max(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = max(dp_max[i-1][j+1]+board[i][j], dp_max[i][j])
            elif j == 1:
                dp_max[i][j] = max(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = max(dp_max[i-1][j+1]+board[i][j], dp_max[i][j])
                dp_max[i][j] = max(dp_max[i-1][j-1]+board[i][j], dp_max[i][j])

            else:
                dp_max[i][j] = max(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = max(dp_max[i-1][j-1]+board[i][j], dp_max[i][j])
    print(max(dp_max[-1]), end=' ')
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp_max[i][j] = min(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = min(dp_max[i-1][j+1]+board[i][j], dp_max[i][j])
            elif j == 1:
                dp_max[i][j] = min(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = min(dp_max[i-1][j+1]+board[i][j], dp_max[i][j])
                dp_max[i][j] = min(dp_max[i-1][j-1]+board[i][j], dp_max[i][j])
            else:
                dp_max[i][j] = min(dp_max[i-1][j]+board[i][j], dp_max[i][j])
                dp_max[i][j] = min(dp_max[i-1][j-1]+board[i][j], dp_max[i][j])

    print(min(dp_max[-1]), end=' ')
