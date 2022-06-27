n = int(input())
dp = [[0] * 2 for i in range(100001)]
dp[1][0] = 1
dp[1][1] = 1

dp[2][0] = 3
dp[2][1] = 2
for i in range(3, 100001):
    dp[i][0] = dp[i-1][0]+2*dp[i-1][1]
    dp[i][1] = dp[i-1][0]+dp[i-1][1]

print((2*dp[n][1] + dp[n][0]) % 9901)

