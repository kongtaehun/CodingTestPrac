n = int(input())
# i-1번째ㄱ까지 구한거 + i-2번째까지 구한거 *2
dp = [0 for i in range(1000)]
dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = dp[i-1]+dp[i-2]*2
print(dp[n-1] % 796796)
