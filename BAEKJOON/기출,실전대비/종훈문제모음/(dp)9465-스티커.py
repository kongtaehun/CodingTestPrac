for i in range(int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(2)]
    dp = [[0]*(n) for i in range(2)]

    # 0,1번째 DP초기화
    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    dp[0][1] = nums[0][1]+nums[1][0]
    dp[1][1] = nums[1][1]+nums[0][0]
    # dp계산
    for i in range(n):
        dp[0][i] = max(dp[1][i-1]+nums[0][i], dp[1][i-2]+nums[0][i])
        dp[1][i] = max(dp[0][i-1]+nums[1][i], dp[0][i-2]+nums[1][i])
    print(max(dp[0][-1], dp[1][-1]))
