n, k = map(int, input().split())
dp = [100000]*(k+1)
nums = []
for i in range(n):
    a = int(input())
    nums.append(a)


for i in range(1, k+1):

    for j in nums:
        if i-j == 0:
            dp[i] = 1
        elif i-j < 0:
            pass
        else:
            dp[i] = min(dp[i], dp[i-j] + 1)

print(dp)
