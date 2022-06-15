from itertools import combinations
n = int(input())
k = int(input())


def setList(n):
    temp = [i for i in range(n+1)]
    nums = []
    nums.append(1)
    for i in range(2, n+1):
        nums.append(i)
        nums.append(i)
        nums.append(i*i)
    for i in list(combinations(temp[2:], 2)):
        nums.append(i[0]*i[1])
        nums.append(i[0]*i[1])
    nums.sort()
    return nums


nums = setList(n)
print(nums[k])
