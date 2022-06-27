n, k = map(int, input().split())
dp = [0]*(k+1)
coins = []
for i in range(n):
    a = int(input())
    coins.append(a)

dp[0] = 1
for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[-1])
