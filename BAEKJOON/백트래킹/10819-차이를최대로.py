from itertools import permutations


def calVal(nums):
    sum = 0
    for i in range(1, len(nums)):
        sum += abs(nums[i]-nums[i-1])
    return sum


n = int(input())
nums = list(map(int, input().split()))

result = 0
for i in list(permutations(nums, n)):
    result = max(result, calVal(i))
print(result)
