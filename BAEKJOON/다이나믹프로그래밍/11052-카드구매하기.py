n = int(input())
nums = [0]+list(map(int, input().split()))
dp = [0 for i in range(n+1)]
for i in range(1, n+1):
    for k in range(0, i):
        dp[i] = max(dp[i], dp[k] + nums[i-k])
print(dp)
