# 점화식 dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
dp = [0]*(12)
n = int(input())
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, n+1):
    dp[i] = sum(dp[i-3:i])
print(dp[n])
