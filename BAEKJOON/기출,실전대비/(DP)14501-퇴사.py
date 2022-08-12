# 뒤에서 부터 선택한다.
n = int(input())
table = [(list(map(int, input().split()))) for i in range(n)]
dp = [0]*(n)
dp.append(0)
for i in range(n-1, -1, -1):
    if i+table[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+table[i][0]]+table[i][1], dp[i+1])
print(dp[0])
