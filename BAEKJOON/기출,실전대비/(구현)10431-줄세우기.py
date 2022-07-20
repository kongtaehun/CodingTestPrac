from bisect import bisect_right
result = []
for i in range(int(input())):
    nums = list(map(int, input().split()))
    test_num = nums[0]
    nums = nums[1:]
    cost = 0
    for i in range(20):
        idx = bisect_right(nums[:i], nums[i])
        if idx != i:
            nums = nums[:idx] + [nums[i]] + nums[idx:i] + nums[i+1:]
            cost += i-idx
    print(test_num, cost)
