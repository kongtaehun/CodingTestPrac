def binary_search(nums, num, n):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == num:
            return True
        if nums[mid] > num:
            end = mid-1
        else:
            start = mid+1
    return False


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
nums2 = list(map(int, input().split()))

for num in nums2:
    print(1 if binary_search(nums, num, n) else 0)
