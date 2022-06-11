# 가장 긴 증가하는 부분수열
n = 7
board = [15, 11, 4, 8, 5, 2, 4]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if board[i] < board[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
 