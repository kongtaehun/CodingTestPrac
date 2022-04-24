n = 7
list = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
dp = [0 for i in range(n)]
maxval = 0
# 뒤에서 부터 채워가다가 1일차에 최댓값이 나오도록
for i in range(n-1, -1, -1):
    time = list[i][0]+i
    if time <= n:
        dp[i] = max(list[i][1]+dp[time], maxval)
        maxval = dp[i]
    else:
        dp[i] = maxval
print(maxval)
