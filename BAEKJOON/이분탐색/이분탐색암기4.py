def getCount(nums, length):
    count = 0
    for i in nums:
        count += i//length
    return count


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        count = getCount(nums, mid)
        if count < target:
            end = mid-1
        else:
            start = mid + 1
    return start


already, needed = map(int, input().split())
nums = []
for i in range(already):
    nums.append(int(input()))
print(binary_search(nums, needed, 1, max(nums))-1)
