from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for num in enumerate(nums[1:]):
    idx = bisect_left(dp, num)
    if idx > len(dp)-1:
        dp.append(num)
print(len(dp))
print(' '.join(list(map(str, dp))))
