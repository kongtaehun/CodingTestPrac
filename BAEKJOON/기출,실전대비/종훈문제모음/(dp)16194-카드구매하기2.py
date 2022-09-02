# 2차원 DP로 해결?
if __name__ == '__main__':
    n = int(input())
    INF = int(1e9)
    nums = list(map(int, input().split()))
    dp = [[INF]*(n) for i in range(n)]
    for i in range(n):
        dp[0][i] = nums[0]*(i+1)

    for i in range(1, n):
        for j in range(n):
            if j < i:
                dp[i][j] = dp[i-1][j]

            elif j-i-1 < 0:
                dp[i][j] = min(nums[i], dp[i-1][j])

            else:
                dp[i][j] = min(dp[i][j-i-1]+nums[i], dp[i-1][j])
    print(dp[-1][-1])
