def calMid(nums, sizeBlu):
    count, suum = 1, 0
    for i in nums:
        if suum+i < sizeBlu:
            suum += i
        else:
            suum = i
            count += 1
    return count


def binarySearch(nums, target, start, end):
    while start <= end:
        mid = (start+end)//2
        count = calMid(nums, mid)

        if count > target:
            start = mid+1
        else:
            end = mid - 1
    return start-1


if __name__ == '__main__':

    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    # 정렬하면안대!!!
    result = binarySearch(nums, m, 0, sum(nums))
    print(max(nums) if result < max(nums) else result)
