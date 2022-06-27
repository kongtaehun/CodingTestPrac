n = int(input())
dp = [[0]*2 for i in range(n+1)]
# [0] ->왼쪽,오른쪽둘다 없을경우
# [1] ->왼쪽
# [2] ->오른쪽
dp[1][0] = 1
dp[1][1] = 1

dp[2][0] = 3
dp[2][1] = 2
for i in range(3, n+1):
    dp[i][0] = dp[i-1][0]+2*dp[i-1][1]
    dp[i][1] = dp[i-1][0]+dp[i-1][1]

print((2*dp[-1][1] + dp[-1][0]) % 9901)
print(dp)
