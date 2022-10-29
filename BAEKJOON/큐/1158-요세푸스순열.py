result = []
n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
start = 0
for i in range(n):
    for _ in range(k-1):
        start += 1
        if start >= len(nums):
            start = 0
    # print(nums[start], start)
    # print(nums)
    result.append(nums[start])
    nums = nums[:start]+nums[start+1:]
    if start >= len(nums):
        start = 0
print('<', end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(str(result[i])+'>', end='')
    else:
        print(str(result[i])+', ', end='')
