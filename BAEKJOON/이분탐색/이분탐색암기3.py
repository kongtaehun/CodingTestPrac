def binarySearch(arr, target, start, end):

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0


n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
nums1.sort()
end = len(nums1)-1
start = 0
for i in nums2:
    print(binarySearch(nums1, i, start, end))
