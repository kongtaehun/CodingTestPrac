dp = [-1]*(123)
strr = input()
for i in range(len(strr)-1, -1, -1):
    dp[ord(strr[i])] = i
for i in range(97, 123):
    print(dp[i], end=' ')
