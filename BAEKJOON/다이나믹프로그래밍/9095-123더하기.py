def get123Count(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, a+1):
            dp[i] = sum(dp[i-3:i])
        return dp[-1]


t = int(input())

nums = []
for i in range(t):
    n = int(input())
    nums.append(n)
    dp = [0]*(n+1)
    print(get123Count(n))
