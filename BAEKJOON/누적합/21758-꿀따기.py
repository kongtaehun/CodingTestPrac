import copy
n = int(input())
nums = [0]+list(map(int, input().split()))
ori_nums = copy.deepcopy(nums)
for i in range(1, n+1):
    nums[i] += nums[i-1]


# 벌벌꿀
bbg_max = 0
first = nums[n]-nums[1]
for i in range(2, n):
    second = nums[n] - nums[i]
    bbg_max = max(bbg_max, first+second-ori_nums[i])
    # print(first, second)
# 벌꿀벌
bgb_max = 0
for i in range(2, n):
    first = nums[i] - nums[1]
    second = nums[n-1] - nums[i-1]
    bgb_max = max(bgb_max, first+second)
    # print(first, second)
# 꿀벌벌
gbb_max = 0
second = nums[n-1]-nums[0]
for i in range(2, n):
    first = nums[i-1] - nums[0]
    gbb_max = max(gbb_max, first+second-ori_nums[i])
    # print(first, second)


print(max(gbb_max, bbg_max, bgb_max))
