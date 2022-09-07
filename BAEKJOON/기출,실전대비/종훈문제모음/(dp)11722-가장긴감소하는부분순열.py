
from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
dp = [nums[0]]
for num in nums[1:]:
    idx = bisect_left(dp, num)
    if idx > len(dp)-1:
        dp.append(num)
    else:
        dp[idx] = num
print(len(dp))
