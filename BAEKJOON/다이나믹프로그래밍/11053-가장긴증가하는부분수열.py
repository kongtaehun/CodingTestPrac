from bisect import bisect_left
# LIS구하기
# 검사하면서 현재 수가 dp의마지막수보다 클경우 append
# 작을 경우 교채한다.()
n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for i in range(n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    elif dp[-1] > nums[i]:
        idx = bisect_left(dp, nums[i])
        dp[idx] = nums[i]
    print(dp)
print(dp)
