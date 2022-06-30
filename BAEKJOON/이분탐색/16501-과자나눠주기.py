import math
import sys
input = sys.stdin.readline


def distribute(arr, maxLen):
    temp = 0
    for len in arr:
        temp += math.floor(len/maxLen)
    return temp


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        count = distribute(arr, mid)
        # print(start, end)
        # print("과자길이가 " + str(mid) + "일 떄" + str(count) + "명")
        if count < target:
            end = mid - 1
        else:
            start = mid+1
    return end


if __name__ == '__main__':
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))

    if sum(nums) < m:
        print(0)

    else:
        print(binarySearch(nums, m, 1, max(nums)))
