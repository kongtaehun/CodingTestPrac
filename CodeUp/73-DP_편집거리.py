# 편집거리 알고리즘이용
a = input()
n = len(a)
b = input()
m = len(b)
dp = [[0]*(m+1) for i in range(n+1)]


for i in range(n+1):
    for j in range(m+1):
        if i == 0:
            dp[i][j] = j
        if j == 0:
            dp[i][j] = i
        print(dp[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

for i in range(n+1):
    for j in range(m+1):

        print(dp[i][j], end=' ')
    print()
