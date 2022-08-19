n = int(input())
times = []
times.append((0, 0))
dp = [0]*(n+2)
for i in range(n):
    duration, pay = map(int, input().split())
    times.append((duration, pay))


for i in range(n, 0, -1):
    if i+times[i][0]-1 <= n:
        dp[i] = max(dp[i+times[i][0]]+times[i][1], dp[i+1])
    else:
        dp[i] = dp[i+1]


print(max(dp))
