import math


def calStudentCount(arr, maxSize):
    temp = 0
    for i in arr:
        temp += math.ceil(i/maxSize)
    return temp


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        student_count = calStudentCount(arr, mid)
        if student_count > target:
            start = mid+1
        else:
            end = mid-1
    return start


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    nums.sort()
    print(binary_search(nums, n, 1, max(nums)))
