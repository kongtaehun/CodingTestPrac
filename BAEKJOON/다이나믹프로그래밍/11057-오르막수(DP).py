n = int(input())
dp = [0]*(n+1)
dp[1] = 10

for i in range(2, n+1):
    sum = 0
    for j in range(11):
        sum += dp[i-1]-j

    dp[i] = sum

print(dp)
