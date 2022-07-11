# 스택으로 구현하면 더쉬워진다는...

n = int(input())
nums = list(map(int, input().split()))

dp = [-1]*(n)
for i in range(1, len(nums)):
    if nums[i] <= nums[i-1]:
        dp[i] = i-1
    else:
        k = 1
        while i-k > 0:
            if nums[i] <= nums[dp[i-k]]:
                dp[i] = dp[i-k]
                break
            else:
                k += 1

for i in dp:
    print(i+1, end=' ')
