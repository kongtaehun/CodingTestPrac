n = int(input())
Non = int(1e9)
dp = [[Non]*10 for i in range(n+1)]

dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]


print(sum(dp[-1]) % 1000000000)
