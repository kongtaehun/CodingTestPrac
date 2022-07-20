# 2차원DP를 이용해야함

strr1 = input()
strr2 = input()
dp = [[0]*(len(strr1)+1) for i in range(len(strr2)+1)]
for i in range(1, len(strr1)+1):
    for j in range(1, len(strr2)+1):
        if strr1[i-1] == strr2[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            # str1이랑 str2중에서 어떤 것이 추가되서 lcs가 결정되는지 모름
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
print(dp)
