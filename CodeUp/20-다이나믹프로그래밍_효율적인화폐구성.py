n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

dp = [0 for i in range(10000)]
for i in coin:
    dp[i] = 1
for i in range(m+1):
    temp = []
    for j in range(len(coin)):
        if dp[i-coin[j]] == 0:
            temp.append(999)
        else:
            temp.append(dp[i-coin[j]]+1)
    dp[i] = min(temp)
print(dp[m-1])
