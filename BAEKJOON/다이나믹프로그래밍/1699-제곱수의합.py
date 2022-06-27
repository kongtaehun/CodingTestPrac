import math
n = int(input())
dp = [100000]*(n+1)
sqr = [i*i for i in range(1, 317)]
for i in range(1, n+1):
    if math.sqrt(i) - int(math.sqrt(i)) == 0:
        dp[i] = 1
        continue
    minVal = dp[i]
    for k in sqr:
        if k < i:
            minVal = min(dp[i-k]+1, minVal)
    dp[i] = minVal
print(dp[-1])
