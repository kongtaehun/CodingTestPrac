def printArr(board):
    print("================")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print("================")


n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dp = [[0]*n for i in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] >= 1 and not (i == n-1 and j == n-1):
            if i+board[i][j] < n and j+board[i][j] < n:
                dp[i+board[i][j]][j] += dp[i][j]
                dp[i][j+board[i][j]] += dp[i][j]
            elif j+board[i][j] < n:
                dp[i][j+board[i][j]] += dp[i][j]
            elif i+board[i][j] < n:
                dp[i+board[i][j]][j] += dp[i][j]


print(dp[-1][-1])
