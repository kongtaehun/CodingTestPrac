n = int(input())


dp = [0]*(91)
dp[1] = 2
dp[2] = 2
dp[3] = 2
dp[4] = 3
for i in range(5, n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])
