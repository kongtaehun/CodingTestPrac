
n = int(input())
nums = list(map(int, input().split()))
dp = [[0]*(n) for i in range(2)]
dp[0][0] = nums[0]
for i in range(1, n):
    dp[0][i] = max(nums[i], dp[0][i-1]+nums[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+nums[i])

# ===예외===
# 1. 모든 수가 음수일 때
# 2. n이 1일 때
flag = 0
for i in nums:
    if i >= 0:
        flag = 1
if n == 1 or flag == 0:
    print(max(nums))
else:
    print(max(max(dp[0]), max(dp[1])))
