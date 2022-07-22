# 점화식 dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
def initDP():
    dp = [0]*(12)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 12):
        dp[i] = sum(dp[i-3:i])


if __name__ == '__main__':
    dp = initDP()
    for i in range(int(input())):
        print(dp[int(input())])
