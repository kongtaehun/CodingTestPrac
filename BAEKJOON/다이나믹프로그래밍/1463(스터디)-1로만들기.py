# i를 3나누기,2나누기,1빼기를 하여  --> dp[i//3],dp[i//2],dp[i-1]
# 그 값의 dp중 가장작은 값으로 초기화
INF = int(1e9)
n = int(input())
dp = [INF]*(int(1e6)+1)

dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    dp[i] = min(dp[i-1]+1, dp[i])

print(dp[n])
