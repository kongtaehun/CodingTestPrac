# true, or false
def twoPointer(arr, l, r, target):
    while l < r:
        temp = arr[l]+arr[r]
        if temp == target:
            return True
        if temp > target:
            r -= 1
        else:
            l += 1
    return False


if __name__ == '__main__':
    result = 0
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(0, len(nums)):
        temp = nums.pop(i)
        result += 1 if twoPointer(nums, 0, len(nums)-1, temp) else 0
        nums.append(temp)
        nums.sort()
    print(result)
